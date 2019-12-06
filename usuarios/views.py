# from django.contrib.auth.models import Group, Permission
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.http import HttpResponse
from usuarios.models import UserConfirm


class CustonLoginView(LoginView):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('users:redirect'))
        return super().dispatch(request, *args, **kwargs)


def email_enviado(request):
    template_name = 'usuarios/emailEnviado.html'
    return render(request, template_name)


def confUser(request, key):
    context = {}
    template_name = "usuarios/confUser.html"
    conf_person = get_object_or_404(UserConfirm.objects.select_related(), key=key)
    user = conf_person.user
    if not conf_person.status(): 
        conf_person.conf()
        user.active()
        context['url_redirect'] = reverse_lazy('cliente:update')    
        return render(request, template_name, context)
    # group = Group.objects.get_or_create(name='new_group')
    return redirect('users:login')


@login_required 
def login_redirect(request):
    if request.user.is_staff:
        return redirect('/admin/')
    else:
        return redirect(reverse_lazy('cliente:update'))
    return redirect('/')
