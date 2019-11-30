from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.http import HttpResponse
from tools.tests import send_mail as s

class IndexView(TemplateView):
    template_name = 'home.html'


def sair(request):
    logout(request)
    return redirect('login')


def enviar_mail_teste(request):
    s()
    return HttpResponse("email enviado")