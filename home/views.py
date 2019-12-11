from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth import logout
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import JsonResponse



class IndexView(TemplateView):
    template_name = 'home.html'


def sair(request):
    logout(request)
    return redirect('login')


# def enviar_mail_teste(request):
#     s()
#     return HttpResponse("email enviado")



class CotratoView(TemplateView):
    template_name = "home/contrato.html"


class ContatoView(View):
    def get(self, request, *args, **kwargs):
        return redirect('/')

    def post(self, request, *args, **kwargs):
        print(request.POST)
        nome = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('message')
        send_mail(
            'Contato hoodid '+ nome,
            nome + "\n\n" + msg,
            email,
            [settings.DEFAULT_EMAIL],
            fail_silently=False,
        )
        return JsonResponse({"msg":"Obrigado! entraremos em contato em breve"})

