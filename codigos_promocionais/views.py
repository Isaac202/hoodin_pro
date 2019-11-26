from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Codigos_Promocionais
from .forms import Codigos_PromocionaisForm, BuscarForm
#from .forms import BuscaPlacerForm


class Codigos_PromocionaisCreate(CreateView):
    model = Codigos_Promocionais
    template_name = "codigos_promocionais/inc_codigos_promocionais.html"
    form_class = Codigos_PromocionaisForm

    success_url = reverse_lazy('lista_servicos')

    def form_valid(self, form):
        form.instance.perfil = self.request.user
        return super(Codigos_PromocionaisCreate, self).form_valid(form)

    #success_url = reverse_lazy('lista_placer')

class Codigos_PromocionaisList(ListView):
    template_name ="codigos_promocionais/listar_codigos_promocionais.html"
    model = Codigos_Promocionais
    paginate_by = 10
    context_object_name = "codigos_promocionais"

    def get_queryset(self):
        qs = Codigos_Promocionais.objects.all()
        promocao = self.request.GET.get('promocao')
        if promocao is not None:
            qs = Codigos_Promocionais.objects.filter(nome__icontains=promocao)
        return qs

    def get_context_data(self, **kwargs):
        context = super(Codigos_PromocionaisList, self).get_context_data(**kwargs)
        form = BuscarForm()
        context['form'] = form
        return context

class Codigos_PromocionaisUpdate(UpdateView):
    model = Codigos_Promocionais
    template_name = "codigos_promocionais/upd_codigos_promocionais.html"
    form_class = Codigos_PromocionaisForm
    success_url = reverse_lazy('lista_codigos_promocionais')

class Codigos_PromocionaisDelete(DeleteView):
    model = Codigos_Promocionais
    template_name = "codigos_promocionais/del_codigos_promocionais.html"
    success_url = reverse_lazy('lista_codigos_promocionais')
