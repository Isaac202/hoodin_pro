from django.urls import path
from home.views import IndexView, ContatoView

app_name = "home"

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contato/', ContatoView.as_view(), name='contato'),
    # path('send-mail', enviar_mail_teste)
]