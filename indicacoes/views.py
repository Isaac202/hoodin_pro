from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Indicacoes
from .forms import IndicacoesForm
from .forms import BuscaForm


class IndicacoesCreate(LoginRequiredMixin, CreateView):
    model = Indicacoes
    template_name = "indicacoes/inc_indicacoes.html"
    form_class = IndicacoesForm
    success_url = reverse_lazy('lista_indicacoes')

    def form_valid(self, form):
        form.instance.perfil = self.request.user
        return super(IndicacoesCreate, self).form_valid(form)


class IndicacoesList(LoginRequiredMixin, ListView):
    template_name ="indicacoes/listar_indicacoes.html"
    model = Indicacoes
    paginate_by = 10
    context_object_name = "indicacoes"

    def get_queryset(self):
        qs = Indicacoes.objects.all()
        busca = self.request.GET.get('busca')
        if busca is not None:
            qs = Indicacoes.objects.filter(nome__icontains=busca)
        return qs

    def get_context_data(self, **kwargs):
        context = super(IndicacoesList, self).get_context_data(**kwargs)
        form = BuscaForm()
        context['form'] = form
        return context


class IndicacoesUpdate(LoginRequiredMixin, UpdateView):
    model = Indicacoes
    template_name = "indicacoes/upd_indicacoes.html"
    form_class = IndicacoesForm
    success_url = reverse_lazy('lista_indicacoes')


class IndicacoesDelete(LoginRequiredMixin, DeleteView):
    model = Indicacoes
    template_name = "indicacoes/del_indicacoes.html"
    success_url = reverse_lazy('lista_indicacoes')