from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Clientes
from .forms import ClientesForm, BuscarForm
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from rest_framework.response import Response

User = get_user_model()


class ClientesCreate(CreateView):
    model = Clientes
    template_name = "clientes/inc_clientes.html"
    form_class = ClientesForm

    success_url = reverse_lazy('lista_clientes')


    #success_url = reverse_lazy('lista_placer')


class ClientesList(LoginRequiredMixin, ListView):
    template_name ="clientes/listar_clientes.html"
    model = Clientes
    paginate_by = 10
    context_object_name = "clientes"

    def get_queryset(self):
        qs = Clientes.objects.all()
        nome_cliente = self.request.GET.get('nome_cliente')
        if nome_cliente is not None:
            qs = Clientes.objects.filter(nome__icontains=nome_cliente)
        return qs

    def get_context_data(self, **kwargs):
        context = super(ClientesList, self).get_context_data(**kwargs)
        form = BuscarForm()
        context['form'] = form
        return context


class ClientesUpdate(LoginRequiredMixin, UpdateView):
    model = Clientes
    template_name = "clientes/upd_clientes.html"
    form_class = ClientesForm
    success_url = reverse_lazy('lista_clientes')


class ClientesDelete(LoginRequiredMixin, DeleteView):
    model = Clientes
    template_name = "clientes/del_clientes.html"
    success_url = reverse_lazy('lista_clientes')
    contexto ={'seleciona_cliente': ClientesForm()}


class ConfirmacaoCadadtro(APIView):

    @csrf_exempt
    def get(self, request):
        resposta = ''

        try:
            if request.method == 'GET':
                chave = request.data.get('chave')
                email = request.data.get('email')
                User.confirmation_key = chave
                if User.is_confirmed:
                    u = User.objects.filter(email=email).update(is_active=True)
                    resposta = 'Seu cadastro na Hoodid foi ativado com sucesso!'
                else:
                    resposta = 'Sua chave está inválida'


                return Response({'msg': resposta})
            else:
                return Response({'msg': 'nao foi post'})

        except Exception as e:
            return Response({'erro': str(e)}, status=401)

