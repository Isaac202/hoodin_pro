from django.urls import path
from home.views import IndexView, ContatoView, BuscarRegistro

app_name = "home"

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('buscar-registro/', BuscarRegistro.as_view(), name='busca'),
    path('contato/', ContatoView.as_view(), name='contato'),
    # path('send-mail', enviar_mail_teste)
]