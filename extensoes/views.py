from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Extensoes
from .forms import ExtensoesForm, BuscarForm
#from .forms import BuscaPlacerForm

#LoginRequiredMixin,
class ExtensoesCreate(CreateView):
    model = Extensoes
    template_name = "extensoes/inc_extensoes.html"
    form_class = ExtensoesForm

    success_url = reverse_lazy('lista_extensoes')

    def form_valid(self, form):
        form.instance.perfil = self.request.user
        return super(ExtensoesCreate, self).form_valid(form)

    #success_url = reverse_lazy('lista_placer')


class ExtensoesList(ListView):
    template_name ="extensoes/listar_extensoes.html"
    model = Extensoes
    paginate_by = 10
    context_object_name = "extensoes"

    def get_queryset(self):
        qs = Extensoes.objects.all()
        nome_extensao = self.request.GET.get('nome_extensao')
        if nome_extensao is not None:
            qs = Extensoes.objects.filter(nome__icontains=nome_extensao)
        return qs

    def get_context_data(self, **kwargs):
        context = super(ExtensoesList, self).get_context_data(**kwargs)
        form = BuscarForm()
        context['form'] = form
        return context


class ExtensoesUpdate(UpdateView):
    model = Extensoes
    template_name = "extensoes/upd_extensoes.html"
    form_class = ExtensoesForm
    success_url = reverse_lazy('lista_extensoes')


class ExtensoesDelete(DeleteView):
    model = Extensoes
    template_name = "extensoes/del_extensoes.html"
    success_url = reverse_lazy('lista_extensoes')