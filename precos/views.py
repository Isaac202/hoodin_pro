from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Precos
from .forms import PrecosForm, BuscarForm
#from .forms import BuscaPlacerForm

#LoginRequiredMixin,
class PrecosCreate(CreateView):
    model = Precos
    template_name = "precos/inc_precos.html"
    form_class = PrecosForm

    success_url = reverse_lazy('lista_precos')

    def form_valid(self, form):
        form.instance.perfil = self.request.user
        return super(PrecosCreate, self).form_valid(form)

    #success_url = reverse_lazy('lista_placer')


class PrecosList(ListView):
    template_name ="precos/listar_precos.html"
    model = Precos
    paginate_by = 10
    context_object_name = "precos"
    '''
    def get_queryset(self):
        qs = Precos.objects.all()
        nome_preco = self.request.GET.get('nome_preco')
        if nome_preco is not None:
            qs = Precos.objects.filter(nome__icontains=nome_preco)

         return qs
'''
    def get_queryset(self):
        qs = Precos.objects.select_related('codservico').all()
        return qs

    def get_context_data(self, **kwargs):
        context = super(PrecosList, self).get_context_data(**kwargs)
        form = BuscarForm()
        context['form'] = form
        return context


class PrecosUpdate(UpdateView):
    model = Precos
    template_name = "precos/upd_precos.html"
    form_class = PrecosForm
    success_url = reverse_lazy('lista_precos')


class PrecosDelete(DeleteView):
    model = Precos
    template_name = "precos/del_precos.html"
    success_url = reverse_lazy('lista_precos')

contexto ={
'seleciona_servico': PrecosForm()
}

