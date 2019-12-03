from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Compras
from .forms import InserirCreditoForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
# Create your views here.


class RtornoView(TemplateView):
    template_name = 'compra_credito/retorno.html'

class CompraCreditoCreate(LoginRequiredMixin, CreateView):

    model = Compras
    template_name = "compras/compra_credito.html"
    form_class = InserirCreditoForm
    #success_url = reverse_lazy('etorno_card')


    def get_success_url(self):
        comp_credito = Compras.objects.filter(id=self.object.id).first()
        msg = str(comp_credito.statu_trasacao)
        self.request.session['msg'] = msg
        return reverse_lazy('retorno_card')

    def form_valid(self, form):
        # form.instance.id_motorista = self.request.user
        print('\n\n\estou aqui')



        return super(CompraCreditoCreate, self).form_valid(form)

