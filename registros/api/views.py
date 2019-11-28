from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from registros.models import Registros, ArquivoRegistro
from registros.forms import RegistrosForm, ArquivoRegistroForm
from registros.api.serializers import ArquivoSerializer
from tools.genereteKey import get_size_file, file_to_shar256


class BasicUploadView(APIView):

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    # def get(self, request, format=None):
    #     data = {}
    #     url = str(reverse_lazy('delete_file', kwargs={'pk':1}))
    #     print(url)
    #     data['url'] = url
    #     return Response(data)

    def post(self, request, format=None):
        file = request.FILES['file']
        name = file.name
        shar256 = file_to_shar256(file)
        size = file.size  # get_size_file(file)
        form = ArquivoRegistroForm(request.POST, request.FILES)
        data = {'is_valid':False}
        if form.is_valid():
            file = form.save(commit=False)
            file.id_usuario = request.user
            file.shar256 = shar256
            file.name = name
            file.size = size
            file.save()
            serializer = ArquivoSerializer(file, many=False)
            data = serializer.data
            data['delete'] = str(reverse_lazy('delete_file', kwargs={'pk':file.pk}))
            data['is_valid'] = True
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