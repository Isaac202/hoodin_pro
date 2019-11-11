from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Registros
from .forms import RegistrosForm


class RegistrosCreate(LoginRequiredMixin, CreateView):
    model = Registros
    template_name = "registros/registros.html"
    form_class = RegistrosForm

    success_url = reverse_lazy('lista_registros')

    def form_valid(self, form):
        form.instance.codusuario = self.request.user
        return super(RegistrosCreate, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(RegistrosCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs
    #success_url = reverse_lazy('lista_placer')


class RegistrosList(LoginRequiredMixin, ListView):
    template_name ="registros/listar_registros.html"
    model = Registros
    paginate_by = 10
    context_object_name = "registros"

    def get_queryset(self):
        qs = Registros.objects.filter(codusuario=self.request.user)
        descricao = self.request.GET.get('descricao')
        if descricao is not None:
            qs = Registros.objects.filter(descricao__icontains=descricao)
        return qs




