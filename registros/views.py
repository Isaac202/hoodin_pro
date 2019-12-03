from django.core.paginator import Paginator
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Registros, ArquivoRegistro
from .forms import RegistrosForm, ArquivoRegistroForm  # , ArquivoRegistroTesteForm
from registros.api.serializers import ArquivoSerializer
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from tools.genereteKey import get_size_file, file_to_shar256
from django.http import HttpResponse
from compras.forms import InserirCreditoForm
from django.contrib import messages
from decimal import Decimal

from cielo.tasks import comprar_credito
from random import randint


class TesteCreateView(View):
    template_name = "registros/teste.html"

    def get(self, request, *args, **kwargs):
        context = {'form': InserirCreditoForm()}
        context["data"] = comprar_credito(10, 'Martoele C. Pixão', '0000000000000001', '279',
                               'Master', '07/2022', 200, 1)
        
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        print(request.POST, '\n\n\n')
        nome_cartao = request.POST.get("nome_cartao")
        numero_cartao = request.POST.get("numero_cartao")
        seguranca = request.POST.get("seguranca")
        bandeira = request.POST.get("bandeira")
        validade = request.POST.get("validade")
        valor = request.POST.get("valor")
        qtd = request.POST.get('qtd_parcela', 1)
        val = Decimal(valor) * 100
        val = int(val)
        pedido = randint(1, 1000000)
        

        # data = comprar_credito(10, nome_cartao, numero_cartao, seguranca, bandeira, validade, val, 1)
        data = comprar_credito(10, 'Martoele C. Pixão', '0662821825086128', '279',
                               'HiperCard', '07/2022', 200, 1)
        
        return render(request, self.template_name,{'data':data})


class RegistrosCreate(LoginRequiredMixin, View):
    template_name = "registros/registro.html"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = {}
        context['form'] = RegistrosForm()
        context['cielo'] = InserirCreditoForm()
        files = ArquivoRegistro.objects.filter(
            id_usuario=self.request.user, paid=False)
        for file in files:
            file.file.delete()
        files.delete()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        files = request.POST.getlist('files', None)
        files = ArquivoRegistro.objects.filter(
            pk__in=files,
            id_usuario=request.user,
            paid=False
        )
        registros = []
        context = {}
        if files.exists():
            msg = "Arquivo(s) registrado(s) com sucesso!"
            messages.success(request, msg)
            for file in files:
                form = RegistrosForm(request.POST)
                if form.is_valid():
                    registro = form.save(commit=False)
                    registro.arquivo = file
                    registro.valor = registro.codservico.preco
                    registro.id_usuario = request.user
                    registro.save()
                    file.paid = True
                    file.save()
                    # registros.append(registro.pk)
        return render(request, self.template_name, context)


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
        queryset = super().get_queryset()
        queryset = Registros.objects.all().select_related()
        paginator = Paginator(queryset, 25)
        page = self.request.GET.get('page', 1)
        registros = paginator.get_page(page)
        return registros
