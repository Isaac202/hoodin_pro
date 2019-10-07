from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Clientes
from .forms import ClientesForm, BuscarForm
#from .forms import BuscaPlacerForm

#LoginRequiredMixin,
class ClientesCreate(CreateView):
    model = Clientes
    template_name = "clientes/inc_clientes.html"
    form_class = ClientesForm

    success_url = reverse_lazy('lista_clientes')


    #success_url = reverse_lazy('lista_placer')


class ClientesList(ListView):
    template_name ="clientes/listar_clientes.html"
    model = Clientes
    paginate_by = 10
    context_object_name = "clientes"

    def get_queryset(self):
        qs = Clientes.objects.all()
        nome_cliente = self.request.GET.get('nome_cliente')
        if nome_cliente is not None:
            qs = Clientes.objects.filter(nome__icontains=nome_cliente)
        return qs

    def get_context_data(self, **kwargs):
        context = super(ClientesList, self).get_context_data(**kwargs)
        form = BuscarForm()
        context['form'] = form
        return context


class ClientesUpdate(UpdateView):
    model = Clientes
    template_name = "clientes/upd_clientes.html"
    form_class = ClientesForm
    success_url = reverse_lazy('lista_clientes')


class ClientesDelete(DeleteView):
    model = Clientes
    template_name = "clientes/del_clientes.html"
    success_url = reverse_lazy('lista_clientes')


contexto ={
'seleciona_cliente': ClientesForm()
}

#https://www.youtube.com/watch?v=wOZz3pgIsNI
#https://www.pythonsetup.com/how-render-django-forms-manually/


