from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Servicos, ServicosExtensoes
from .forms import ServicosForm, ServicosExtensoesForm, BuscarForm
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
    template_name = "servicos/inc_servicosextensoes.html"
    form_class = ServicosExtensoesForm

    success_url = reverse_lazy('lista_servicos')

    '''
            def dispatch(self, request, *args, **kwargs):
                self.codservico = kwargs['codservico']
                self.request.session['codservico'] = kwargs['codservico']
                servicos = Servicos.objects.filter(id=self.codservico).first()
                request.session['nome_servico'] = servicos.nome
                #request.session['codigo_servico'] = servicos.codservico

                return super().dispatch(request, *args, **kwargs)
    '''

    def form_valid(self, form):
        form.instance.perfil = self.request.user
        return super(ServicosExtensoesCreate, self).form_valid(form)
