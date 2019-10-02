from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Servicos, ServicosExtensoes
from .forms import ServicosForm, BuscarForm, ServicosExtensoesForms, BuscarExtensoesForm
#from .forms import BuscaPlacerForm


class ServicosCreate(CreateView):
    model = Servicos
    template_name = "servicos/inc_servicos.html"
    form_class = ServicosForm

    success_url = reverse_lazy('lista_servicos')

    def form_valid(self, form):
        form.instance.perfil = self.request.user
        return super(ServicosCreate, self).form_valid(form)

    #success_url = reverse_lazy('lista_placer')

class ServicosList(ListView):
    template_name ="servicos/listar_servicos.html"
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

class ServicosExtensoesCreate(CreateView):
    model = ServicosExtensoes
    template_name = 'servicos/inc_servicosextensoes.html'
    form_class = ServicosExtensoesForms
    success_url = reverse_lazy('lista_servicosextensoes')

    def dispatch(self, request, *args, **kwargs):
        self.codservico = kwargs['codservico']
        self.request.session['codservico'] = kwargs['codservico']
        servicos = Servicos.objects.filter(id= self.codsevico).first()
        request.session['nome_servicos'] = servicos.nome

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.codservico = Servicos.objects.get(id=self.codservico)
        return super(ServicosExtensoesCreate, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(ServicosExtensoesCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class ServicosExtensoesList(ListView):
    template_name ="servicos/listar_servicosextensoes.html"
    model = ServicosExtensoes
    paginate_by = 10
    context_object_name = "servicosextensoes"

    def get_queryset(self):
        codservico = self.request.session['codservico']
        qs = ServicosExtensoes.objects.select_related('codservico').filter(codservico=codservico)
        nome = self.request.GET.get('nome')

        if nome is not None:
            qs = ServicosExtensoes.objects.filter(codservico=codservico, nome__icontains=nome)

        return qs

    def get_context_data(self, **kwargs):
        context = super(ServicosExtensoesList, self).get_context_data(**kwargs)
        form = BuscarExtensoesForm()
        context['form'] = form
        return context

class ServicosExtensoesUpdate(UpdateView):
    model = ServicosExtensoes
    form_class = ServicosExtensoesForms
    template_name = "servicos/upd_servicosextensoes.html"
    success_url = reverse_lazy('lista_servicosextensoes')

    def get_form_kwargs(self):
        kwargs = super(ServicosExtensoesUpdate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

'''
class CampAnuncioList(LoginRequiredMixin, ListView):
    template_name = 'campanha/listar_camp_anuncios.html'
    model = Anuncio
    context_object_name = "camp_anuncios"

    def get_queryset(self):
        codigo_campnha = self.request.session['codigo_campanha']
        qs = Anuncio.objects.select_related('id_campanha').filter(id_campanha=codigo_campnha).order_by('nome')

        return qs
    def dispatch(self, request, *args, **kwargs):
        self.id_campanha= kwargs['codigo_campanha']
        self.request.session['codigo_campanha'] = kwargs['codigo_campanha']
        return super().dispatch(request, *args, **kwargs)
'''