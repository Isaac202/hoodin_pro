from django.urls import path
from home.views import IndexView, enviar_mail_teste

app_name = "home"

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('send-mail', enviar_mail_teste)
]