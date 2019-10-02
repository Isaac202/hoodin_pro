from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Area_Atuacao
from .forms import Area_AtuacaoForm, BuscarForm
#from .forms import BuscaPlacerForm

#LoginRequiredMixin,
class Area_AtuacaoCreate(CreateView):
    model = Area_Atuacao
    template_name = "area_atuacao/inc_area_atuacao.html"
    form_class = Area_AtuacaoForm

    success_url = reverse_lazy('lista_area_atuacao')

    def form_valid(self, form):
        form.instance.perfil = self.request.user
        return super(Area_AtuacaoCreate, self).form_valid(form)

    #success_url = reverse_lazy('lista_placer')


class Area_AtuacaoListCriacaoPublicitaria(ListView):
    template_name ="area_atuacao/listar_area_atuacao.html"
    model = Area_Atuacao
    paginate_by = 10
    context_object_name = "area_atuacao"

    def get_queryset(self):
        qs = Area_Atuacao.objects.all()
        nome_area_atuacao = self.request.GET.get('nome_area_atuacao')
        if nome_area_atuacao is not None:
            qs = Area_Atuacao.objects.filter(nome__icontains=nome_area_atuacao)
        return qs

    def get_context_data(self, **kwargs):
        context = super(Area_AtuacaoList, self).get_context_data(**kwargs)
        form = BuscarForm()
        context['form'] = form
        return context

class Area_AtuacaoList(ListView):
    template_name ="area_atuacao/listar_area_atuacao_criacaopublicitaria.html"
    model = Area_Atuacao
    paginate_by = 10
    context_object_name = "area_atuacao"

    def get_queryset(self):
        qs = Area_Atuacao.objects.all()
        nome_area_atuacao = self.request.GET.get('nome_area_atuacao')
        if nome_area_atuacao is not None:
            qs = Area_Atuacao.objects.filter(nome__icontains=nome_area_atuacao)
        return qs

    def get_context_data(self, **kwargs):
        context = super(Area_AtuacaoList, self).get_context_data(**kwargs)
        form = BuscarForm()
        context['form'] = form
        return context


class Area_AtuacaoUpdate(UpdateView):
    model = Area_Atuacao
    template_name = "area_atuacao/upd_area_atuacao.html"
    form_class = Area_AtuacaoForm
    success_url = reverse_lazy('lista_area_atuacao')


class Area_AtuacaoDelete(DeleteView):
    model = Area_Atuacao
    template_name = "area_atuacao/del_area_atuacao.html"
    success_url = reverse_lazy('lista_area_atuacao')