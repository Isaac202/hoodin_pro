from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Instituicoes
from .forms import InstituicoesForm, BuscarForm
#from .forms import BuscaPlacerForm

#LoginRequiredMixin,
class InstituicoesCreate(CreateView):
    model = Instituicoes
    template_name = "instituicoes/inc_instituicoes.html"
    form_class = InstituicoesForm

    success_url = reverse_lazy('lista_instituicoes')

    def form_valid(self, form):
        form.instance.perfil = self.request.user
        return super(InstituicoesCreate, self).form_valid(form)

    #success_url = reverse_lazy('lista_placer')


class InstituicoesList(ListView):
    template_name ="instituicoes/listar_instituicoes.html"
    model = Instituicoes
    paginate_by = 10
    context_object_name = "instituicoes"

    def get_queryset(self):
        qs = Instituicoes.objects.all()
        nome_instituicao = self.request.GET.get('nome_instituicao')
        if nome_instituicao is not None:
            qs = Instituicoes.objects.filter(nome__instituicao=nome_instituicao)
        return qs

    def get_context_data(self, **kwargs):
        context = super(InstituicoesList, self).get_context_data(**kwargs)
        form = BuscarForm()
        context['form'] = form
        return context


class InstituicoesUpdate(UpdateView):
    model = Instituicoes
    template_name = "instituicoes/upd_instituicoes.html"
    form_class = InstituicoesForm
    success_url = reverse_lazy('lista_instituicoes')


class InstituicoesDelete(DeleteView):
    model = Instituicoes
    template_name = "insituicoes/del_instituicoes.html"
    success_url = reverse_lazy('lista_instituicoes')