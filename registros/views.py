from weasyprint.fonts import FontConfiguration
from weasyprint import HTML
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Registros, ArquivoRegistro
# , ArquivoRegistroTesteForm
from .forms import RegistrosForm, RegistrosViewForm, ArquivoRegistroForm
from registros.api.serializers import ArquivoSerializer
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from tools.genereteKey import get_size_file, file_to_shar256
from django.http import HttpResponse
from compras.forms import InserirCreditoForm
from django.contrib import messages
from decimal import Decimal
from django.db.models import Sum
from cielo.tasks import comprar_credito
from random import randint
from codigos_promocionais.utils import set_codigo_promocional
from usuarios.models import Confuguracao


class TesteCreateView(View):
    template_name = "compras/compra_concluida.html"

    def get(self, request, *args, **kwargs):
        msg = "Arquivo(s) registrado(s) com sucesso!"
        messages.success(request, msg)
        return render(request, self.template_name)


class RegistrosCreate(LoginRequiredMixin, View):
    template_name = "registros/registro.html"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = {}
        servico_digitalizacao = bool(request.GET.get('sd'))
        # print(servico_digitalizacao,'\n\n')
        context['form'] = RegistrosViewForm(sd=servico_digitalizacao)
        context['cielo'] = InserirCreditoForm()
        files = ArquivoRegistro.objects.filter(
            id_usuario=self.request.user, paid=False)
        for file in files:
            file.file.delete()
        files.delete()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        cliente = request.user.clientes
        save = request.POST.get('save_file', None)
        files = request.POST.getlist('files', None)
        code = request.POST.get('codigo_promocional', None)
        if code:
            code = set_codigo_promocional(code, cliente)
        files = ArquivoRegistro.objects.filter(
            pk__in=files,
            id_usuario=request.user,
            paid=False
        )
        manter_arquivo = False
        if files.exists():
            self.template_name = "compras/compra_concluida.html"
            valor = files.aggregate(total=Sum('value'))["total"]
            if save:
                manter_arquivo = True
                conf = Confuguracao.objects.first()
                valor += conf.valor_file * files.count()
            valor_credito_cliente = cliente.valor_credito
            if code:
                valor_credito_cliente += code.valor
            if valor_credito_cliente >= valor:
                cliente.valor_credito = valor_credito_cliente - valor
                cliente.save()
                if code:
                    msg = "Código promocional resgatado!"
                    messages.success(request, msg)
                msg = "Arquivo(s) registrado(s) com sucesso!"
                messages.success(request, msg)
                for file in files:
                    form = RegistrosForm(request.POST)
                    if form.is_valid():
                        registro = form.save(commit=False)
                        registro.arquivo = file
                        registro.valor = registro.codservico.preco
                        registro.id_usuario = request.user
                        registro.id_cliente = cliente
                        registro.manter_arquivo = manter_arquivo
                        registro.descricao = file.resume
                        registro.save()
                        file.paid = True
                        file.save()
            else:
                msg = "Saldo Insuficiente!"
                messages.error(request, msg)
                files.delete()

        return self.get(request, *args, **kwargs)


class RegistrosList(LoginRequiredMixin, ListView):
    template_name = "registros/listar_registros.html"
    model = Registros
    paginate_by = 10
    context_object_name = "registros"

    def get_queryset(self):
        qs = Registros.objects.filter(id_usuario=self.request.user)
        descricao = self.request.GET.get('descricao')
        if descricao is not None:
            qs = Registros.objects.filter(descricao__icontains=descricao)
        return qs


class BasicUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        return render(self.request, 'photos/basic_upload/index.html', {'photos': photos_list})

    def post(self, request):
        file = request.FILES['file']
        name = file.name
        shar256 = file_to_shar256(file)
        size = file.size  # get_size_file(file)
        form = ArquivoRegistroForm(request.POST, request.FILES)
        data = {'is_valid': True, 'name': "erro", 'size': size, "key": shar256}
        if form.is_valid():
            file = form.save(commit=False)
            file.id_usuario = request.user
            file.shar256 = shar256
            file.name = name
            file.size = size
            file.save()
            data = {'is_valid': True, 'name': file.name,
                    'size': size, "key": shar256}

        return JsonResponse(data)


class MeusRegistrosList(ListView):
    model = Registros
    context_object_name = 'registros'
    template_name = 'registros/meus_registros.html'

    def get_queryset(self):
        de = self.request.GET.get('de', None)
        ate = self.request.GET.get('ate', None)
        title = self.request.GET.get('title', None)
        page = self.request.GET.get('page', 1)
        queryset = super().get_queryset()
        queryset = Registros.objects.filter(
            id_usuario=self.request.user).select_related()
        if de:
            queryset = queryset.filter(data__gte=de)
        if ate:
            queryset = queryset.filter(data__lte=ate)
        if title:
            queryset = queryset.filter(arquivo__resume__contains=title)
        else:
            paginator = Paginator(queryset, 8)
            queryset = paginator.get_page(page)
        return queryset


# # -*- coding: UTF-8 -*-
# from __future__ import unicode_literals


# from .models import Donation


@login_required
def to_pdf(request, id_registro):
    registro = get_object_or_404(
        Registros, pk=id_registro, id_usuario=request.user)
    response = HttpResponse(content_type="application/pdf")
    # response['Content-Disposition'] = "teste.pdf"
    # )
    context = []
    coautores = registro.arquivo.coautores_set.all()
    cont = coautores.count()
    for c in range(0, cont):
        salt = 5
        index = (c+1) * salt
        if index < cont:
            # print(index-salt, index)
            context.append(coautores[index-salt: index])
        else:
            # print(index-salt, cont)
            context.append(coautores[index-salt:cont])
            break
    html = render_to_string("registros/certificado.html", {
        'registro': registro,
        'lista_coautores': context
    })

    font_config = FontConfiguration()
    HTML(string=html).write_pdf(response, font_config=font_config)
    return response
