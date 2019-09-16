from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import logout

class IndexView(TemplateView):
    template_name = 'home/index.html'


def sair(request):
    logout(request)
    return redirect('login')
