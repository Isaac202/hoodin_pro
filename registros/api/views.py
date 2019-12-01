from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from registros.models import Registros, ArquivoRegistro
from registros.forms import RegistrosForm, ArquivoRegistroForm
from registros.api.serializers import ArquivoSerializer
from tools.genereteKey import get_size_file, file_to_shar256
from servicos.models import Servicos
from django.shortcuts import get_object_or_404
from django.utils import timezone


class BasicUploadView(APIView):

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    # def get(self, request, format=None):
        # data = {}
        # url = str(reverse_lazy('delete_file', kwargs={'pk':1}))
        # print(url)
        # data['url'] = url
        # request.session['files'].append(1)
        # data = request.session['files']
        # return Response(data)

    def post(self, request, format=None):
        service = request.GET.get('service')
        service = get_object_or_404(Servicos, pk=service)
        cliente = request.user.clientes
        file = request.FILES['file']
        data = {'is_valid': False}
        name = file.name
        shar256 = file_to_shar256(file)
        size = file.size  # get_size_file(file)
        form = ArquivoRegistroForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.id_usuario = request.user
            file.shar256 = shar256
            file.name = name
            file.size = size
            file.save()
            serializer = ArquivoSerializer(file, many=False)
            data = serializer.data
            data['delete'] = str(reverse_lazy('delete_file', kwargs={'pk': file.pk}))
            data['is_valid'] = True

        files = ArquivoRegistro.objects.filter(
            id_usuario=request.user, paid=False
        )

        price = service.preco * files.count()
        data['price'] = price
        # data['post'] = request.POST

        # if not cliente.valor_credito >= price:
        #     data['error'] = "Crédito insuficiente"
        return Response(data)


class SetResumeFileView(APIView):

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def post(self, request, pk, format=None):
        data = {'success': False}
        file = ArquivoRegistro.objects.filter(pk=pk, id_usuario=request.user)
        if file.exists():
            file.update(resume=request.POST['resume'])
            # file.resume =
            # file.save()
            data['success'] = True
        return Response(data)


class DeleteFileView(APIView):

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def post(self, request, pk, format=None):
        data = {'success': False}
        file = ArquivoRegistro.objects.filter(pk=pk, id_usuario=request.user)
        if file.exists():
            file = file.first()
            file.file.delete()
            file.delete()
            data['success'] = True
        return Response(data)
