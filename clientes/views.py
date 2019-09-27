from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Clientes
from indicacoes.models import Indicacoes
from .forms import ClientesForm
#from .forms import BuscaPlacerForm


class ClientesCreate(CreateView):
    model = Clientes
    template_name = "clientes/inc_clientes.html"
    form_class = ClientesForm

    success_url = reverse_lazy('lista_clientes')

    def form_valid(self, form):
        form.instance.perfil = self.request.user
        return super(ClientesCreate, self).form_valid(form)

    #success_url = reverse_lazy('lista_placer')


class ClientesList(ListView):
    template_name ="clientes/listar_clientes.html"
    model = Clientes
    paginate_by = 10
    context_object_name = "clientes"


class ClientesUpdate(UpdateView):
    model = Clientes
    template_name = "clientes/upd_clientes.html"
    form_class = ClientesForm
    success_url = reverse_lazy('lista_clientes')


class ClientesDelete(DeleteView):
    model = Clientes
    template_name = "clientes/del_clientes.html"
    success_url = reverse_lazy('lista_clientes')

class SelecionaInidicacoes(ListView):
    template_name = 'clientes/lista_indicacoes.html'
    model = Clientes
    context_object_name = "seleciona_indicacoes"

contexto ={
'seleciona_indicacao': ClientesForm()
}

#https://www.youtube.com/watch?v=wOZz3pgIsNI
#https://www.pythonsetup.com/how-render-django-forms-manually/


