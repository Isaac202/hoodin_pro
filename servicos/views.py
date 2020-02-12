from decimal import Decimal
from django.db.models import F
import json
import requests
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Servicos
from .forms import ServicosForm, BuscarForm
from django.conf import settings
# from .forms import BuscaPlacerForm


class ServicosCreate(CreateView):
    model = Servicos
    template_name = "servicos/inc_servicos.html"
    form_class = ServicosForm

    success_url = reverse_lazy('lista_servicos')

    def form_valid(self, form):
        form.instance.perfil = self.request.user
        return super(ServicosCreate, self).form_valid(form)

    # success_url = reverse_lazy('lista_placer')


class ServicosList(ListView):
    template_name = "servicos/listar_servicos.html"
    model = Servicos
    paginate_by = 10
    context_object_name = "servicos"

    def get_queryset(self):
        qs = Servicos.objects.all()
        nome_servico = self.request.GET.get('nome_servico')
        if nome_servico is not None:
            qs = Servicos.objects.filter(nome__icontains=nome_servico)
        return qs

    def get_context_data(self, **kwargs):
        context = super(ServicosList, self).get_context_data(**kwargs)
        form = BuscarForm()
        context['form'] = form
       # context['nomeservico'] = 'nome do servico'
        # context['codservico'] = 1
        return context


class ServicosUpdate(UpdateView):
    model = Servicos
    template_name = "servicos/upd_servicos.html"
    form_class = ServicosForm
    success_url = reverse_lazy('lista_servicos')


class ServicosDelete(DeleteView):
    model = Servicos
    template_name = "servicos/del_servicos.html"
    success_url = reverse_lazy('lista_servicos')


# class ServicosExtensoesCreate(CreateView):
#     model = ServicosExtensoes
#     template_name = "servicos/inc_servicosextensoes.html"
#     form_class = ServicosExtensoesForm

#     success_url = reverse_lazy('lista_servicos')

#     def dispatch(self, request, *args, **kwargs):
#         #self.codservico = kwargs['id']
#         #self.request.session['codservico'] = kwargs['id']
#         #servicos = Servicos.objects.filter(id=self.codservico).first()
#         #request.session['nome_servico'] = servicos.nome
#         #request.session['codigo_servico'] = servicos.codservico
#         return super().dispatch(request, *args, **kwargs)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['codservico'] = self.request.GET.get('codservico',None)
#         context['nomeservico'] = self.request.GET.get('nomeservico',None)
#         return context

#     def form_valid(self, form):
#         form.instance.perfil = self.request.user
#         return super(ServicosExtensoesCreate, self).form_valid(form)

from usuarios.models import Confuguracao

class TabelaPrecos(TemplateView):
    template_name = "servicos/tabela.html"

    def dispatch(self, request, *args, **kwargs):
        try:
            url = "https://economia.awesomeapi.com.br/all/USD-BRL,EUR-BRL"
            response = requests.get(url)
            data = response.text
            parsed = json.loads(data)
            self.euro = Decimal(parsed['EUR']["ask"])
            self.dolar = Decimal(parsed['USD']["ask"])
        except:
            conf = Confuguracao.objects.first()
            self.euro = conf.euro
            self.dolar = conf.dolar
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dolar'] = self.dolar
        context['euro'] = self.euro
        context["servicos"] = Servicos.objects.filter(servico_digitalizacao=False).annotate(
            dolar=F("preco")/self.dolar, euro=F('preco')/self.euro)
        return context
