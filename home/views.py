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
from registros.models import Registros



class IndexView(TemplateView):
    template_name = 'home.html'

    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return redirect('/admin')
        return super().dispatch(request, *args, **kwargs)
    


def sair(request):
    logout(request)
    return redirect('login')


# def enviar_mail_teste(request):
#     s()
#     return HttpResponse("email enviado")


class BuscarRegistro(View):
    template_name = "home/buscar.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        context = {}
        context['busca'] = True
        code = request.POST.get('code', None)
        if code:
            context['code'] = code
            context['r'] = Registros.objects.filter(arquivo__code=code).first()
            
        return render(request, self.template_name, context)


class CotratoView(TemplateView):
    template_name = "home/contrato.html"


class ContatoView(View):
    template_name = "home/contato_page.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        # print(request.POST)
        nome = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('message')
        try:
            send_mail(
                'Contato hoodid '+ nome,
                nome + "\n\n" + msg,
                email,
                [settings.DEFAULT_EMAIL],
                fail_silently=False,
            )
            return JsonResponse({"msg":"Obrigado! entraremos em contato em breve"})
        except:
            return JsonResponse({"msg":"Ops! algo deu errado :("})
