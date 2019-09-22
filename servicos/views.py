from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Servicos
from .forms import ServicosForm
#from .forms import BuscaPlacerForm


class ServicosCreate(LoginRequiredMixin, CreateView):
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


class ServicosUpdate(LoginRequiredMixin, UpdateView):
    model = Servicos
    template_name = "servicos/upd_servicos.html"
    form_class = ServicosForm
    success_url = reverse_lazy('lista_servicos')


class ServicosDelete(LoginRequiredMixin, DeleteView):
    model = Servicos
    template_name = "servicos/del_servicos.html"
    success_url = reverse_lazy('lista_servicos')