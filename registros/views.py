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
import datetime
# from weasyprint import HTML
# from weasyprint.fonts import FontConfiguration

class TesteCreateView(View):
    template_name = "registros/certificado.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


# from registros.tasks import signature
from tools.bry import signature_files

class RegistrosCreate(LoginRequiredMixin, View):
    template_name = "registros/registro.html"

    def get(self, request, *args, **kwargs):
        context = {}
        servico_digitalizacao = bool(request.GET.get('sd'))
        # print(servico_digitalizacao,'\n\n')
        vsf = Confuguracao.objects.first().valor_file
        vsf = "%.2f" % vsf
        context['sd'] = servico_digitalizacao
        context['vsf'] = vsf.replace(',', '.')
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
        pk_files = request.POST.getlist('files', None)
        code = request.POST.get('codigo_promocional', None)
        conf = Confuguracao.objects.first()
        if not conf:
            return HttpResponse('Ops! ocorreu um erro interno, algumas configurações não foram definidas.')
        if code:
            code = set_codigo_promocional(code, cliente)
        files = ArquivoRegistro.objects.filter(
            pk__in=pk_files,
            id_usuario=request.user,
            paid=False
        ).order_by('id')
        manter_arquivo = False 
        if files.exists():
            self.template_name = "compras/compra_concluida.html"
            valor = files.aggregate(total=Sum('value'))["total"]
            if save:
                manter_arquivo = True
                valor += conf.valor_file * files.count()
            valor_credito_cliente = cliente.valor_credito
            if code:
                valor_credito_cliente += code.valor
            if valor_credito_cliente >= valor:
                assinados = signature_files(pk_files)
                if assinados:
                    pontos = cliente.pontuacao + ((valor * conf.percentual)/100)
                    cliente.pontuacao = pontos
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
                    self.template_name = "compras/erro.html"
                    msg = "Desculpe houve um erro inesperado! :("
                    messages.error(request, msg)
                    files.delete()
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


class BasicUploadView(LoginRequiredMixin, View):
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


class MeusRegistrosList(LoginRequiredMixin, ListView):
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
            excluido=False,
            id_usuario=self.request.user).select_related()
        if de:
            queryset = queryset.filter(data__gte=de)
        if ate:
            ate = datetime.datetime.strptime(ate, "%Y-%m-%d")
            ate = ate + datetime.timedelta(days=1)
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

from django_pdfkit import PDFView

class CertificadoPDFView(LoginRequiredMixin, PDFView):
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_registro = kwargs['id_registro']
        registro = get_object_or_404(
        Registros, pk=id_registro, id_usuario=self.request.user)
        c_autores = []
        coautores = registro.arquivo.coautores_set.all()
        if coautores:
            cont = coautores.count()
            for c in range(0, cont):
                salt = 5
                index = (c+1) * salt
                if index < cont:
                    c_autores.append(coautores[index-salt: index])
                else:
                    c_autores.append(coautores[index-salt:cont])
                    break
        context["registro"] = registro
        context["lista_coautores"] = c_autores
        return context
    
