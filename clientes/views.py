from django.http import HttpResponseRedirect
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
from django.contrib.messages.views import SuccessMessageMixin

User = get_user_model()


class ClientesCreate(SuccessMessageMixin, CreateView):
    model = Clientes
    template_name = "clientes/inc_clientes.html"
    form_class = ClientesForm
    success_url = reverse_lazy('lista_clientes')
    success_message = "Verifique seu email pra ativar seu cadastro!"


class ClientesList(LoginRequiredMixin, ListView):
    template_name ="clientes/listar_clientes.html"
    model = Clientes
    paginate_by = 10
    context_object_name = "clientes"

    def get_queryset(self):

        qs = Clientes.objects.filter(codusuario=self.request.user)
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
                chave = self.request.query_params.get('chave', None)
                email = self.request.query_params.get('email', None)
                if chave:

                    if Clientes.objects.filter(confirmation_key=chave).exists():
                        usuario_novo = User.objects.filter(email=email).update(is_active=True)
                        return HttpResponseRedirect(redirect_to='https://registrosonline.com.br/accounts/login/')
                    else:
                          resposta = 'Sua chave está inválida'
                else:
                    resposta = 'Sua chave está inválida'

                return HttpResponseRedirect(redirect_to='https://registrosonline.com.br/accounts/login/')
            else:
                return Response({'msg': 'erro'})

        except Exception as e:
            return Response({'erro': str(e)}, status=401)

