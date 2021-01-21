from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Avaliadores
from .forms import CreateAvaliadoresForm
from .forms import BuscaAvaliadoresForm


class AvaliadoresCreate(LoginRequiredMixin, CreateView):
    model = Avaliadores
    template_name = "avaliadores/inc_avaliadores.html"  
    form_class = CreateAvaliadoresForm
    success_url = reverse_lazy('lista_avaliadores')

    def form_valid(self, form):
        form.instance.perfil = self.request.user
        return super(AvaliadoresCreate, self).form_valid(form)


class AvaliadoresList(LoginRequiredMixin, ListView):
    template_name ="avaliadores/listar_avaliadores.html"
    model = Avaliadores
    paginate_by = 10
    context_object_name = "avaliadores"

    def get_queryset(self):
        qs = Avaliadores.objects.filter(perfil=self.request.user)
        busca = self.request.GET.get('busca')
        if busca is not None:
            qs = Avaliadores.objects.filter(perfil=self.request.user, nome__icontains=busca)
        return qs

    def get_context_data(self, **kwargs):
        context = super(AvaliadoresList, self).get_context_data(**kwargs)
        form = BuscaAvaliadoresForm()
        context['form'] = form
        return context


class AvaliadoresUpdate(LoginRequiredMixin, UpdateView):
    model = Avaliadores
    template_name = "avaliadores/upd_avaliadores.html"
    form_class = CreateAvaliadoresForm
    success_url = reverse_lazy('lista_avaliadores')


class AvaliadoresDelete(LoginRequiredMixin, DeleteView):
    model = Avaliadores
    template_name = "avaliadores/confirma_delete.html"
    success_url = reverse_lazy('lista_avaliadores')


# Create your views here.
