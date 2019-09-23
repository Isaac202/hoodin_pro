from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Indicacoes
from .forms import IndicacoesForm
#from .forms import BuscaPlacerForm

#LoginRequiredMixin,
class IndicacoesCreate(CreateView):
    model = Indicacoes
    template_name = "indicacoes/inc_indicacoes.html"
    form_class = IndicacoesForm

    success_url = reverse_lazy('lista_indicacoes')

    def form_valid(self, form):
        form.instance.perfil = self.request.user
        return super(IndicacoesCreate, self).form_valid(form)

    #success_url = reverse_lazy('lista_placer')


class IndicacoesList(ListView):
    template_name ="indicacoes/listar_indicacoes.html"
    model = Indicacoes
    paginate_by = 10
    context_object_name = "indicacoes"


class IndicacoesUpdate(UpdateView):
    model = Indicacoes
    template_name = "indicacoes/upd_indicacoes.html"
    form_class = IndicacoesForm
    success_url = reverse_lazy('lista_indicacoes')


class IndicacoesDelete(DeleteView):
    model = Indicacoes
    template_name = "indicacoes/del_indicacoes.html"
    success_url = reverse_lazy('lista_indicacoes')