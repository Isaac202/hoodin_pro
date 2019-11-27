from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Registros, ArquivoRegistro
from .forms import RegistrosForm, ArquivoRegistroForm
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from tools.genereteKey import get_size_file, file_to_shar256

class RegistrosCreate( CreateView):
    model = Registros
    template_name = "registros/registros.html"
    form_class = RegistrosForm

    success_url = reverse_lazy('lista_registros')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["files"] =  ArquivoRegistro.objects.filter(id_usuario=self.request.user)
        return context
    

    def form_valid(self, form):
        form.instance.id_usuario = self.request.user
        return super(RegistrosCreate, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(RegistrosCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs
    #success_url = reverse_lazy('lista_placer')


class RegistrosList(LoginRequiredMixin, ListView):
    template_name ="registros/listar_registros.html"
    model = Registros
    paginate_by = 10
    context_object_name = "registros"

    def get_queryset(self):
        qs = Registros.objects.filter(id_usuario=self.request.user)
        descricao = self.request.GET.get('descricao')
        if descricao is not None:
            qs = Registros.objects.filter(descricao__icontains=descricao)
        return qs


class BasicUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        return render(self.request, 'photos/basic_upload/index.html', {'photos': photos_list})

    def post(self, request):
        file = request.FILES['file']
        name = file.name
        shar256 = file_to_shar256(file)
        size  = file.size #get_size_file(file)
        form = ArquivoRegistroForm(request.POST, request.FILES)
        data = {'is_valid': True, 'name': "erro", 'size': size, "key":shar256}
        if form.is_valid():
            file = form.save(commit=False)
            file.id_usuario = request.user
            file.shar256 = shar256
            file.name = name
            file.size = size
            file.save()
            data = {'is_valid': True, 'name': file.name, 'size': size, "key":shar256}
        
        # data = {'is_valid': False}
        return JsonResponse(data)