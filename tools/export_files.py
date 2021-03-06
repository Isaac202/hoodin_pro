from codigos_promocionais.utils import check_codigo_promocionanl
from random import randint
from compras.models import Compras
from cielo.tasks import comprar_credito
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from usuarios.models import Confuguracao
from django.urls import reverse_lazy
from registros.models import Registros, ArquivoRegistro
from registros.forms import RegistrosForm, RegistrosViewForm, ArquivoRegistroForm
from registros.api.serializers import ArquivoSerializer
from tools.genereteKey import file_path_to_shar256
from servicos.models import Servicos
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.db.models import Sum
from decimal import Decimal
from django.core.files import File
from django.contrib.auth import get_user_model as g
import os

# django.core.files.uploadedfile.InMemoryUploadedFile

def atualizar_senha():
    users = g().objects.all()
    print('atualizando')
    for user in users:
        user.set_password(user.password)
        user.save()

def file_size(fname):
        import os
        statinfo = os.stat(fname)
        return statinfo.st_size

# user = g().objects.first()

BASE_DIR_EX = "/home/drummerzzz/workspace/python/teste"

def export(BASE_DIR):
    # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    print(BASE_DIR)
    paths = os.listdir(BASE_DIR)
    for path in paths:
        # pks = path.split('-')
        if path not in 'path.py':
            registro = Registros.objects.filter(codregistro=int(path))
            # result = registro.exists()
            # r = registro[0]
            if registro.exists():# and r.arquivo is None:
                # print(registro[0])
                r = registro.first()
                user = r.id_usuario
                for subpath, _, arquivos in os.walk(os.path.join(BASE_DIR, path)):
                    myfile = ArquivoRegistro()
                    myfile.codregistro= int(path)
                    myfile.id_usuario = user
                    myfile.value = Decimal('0')
                    myfile.paid = True
                    myfile.resume = registro[0].descricao
                    myfile.save()
                    r.arquivo = myfile
                    r.save()
                    # myfile.size = 123# os.fstat(f.fileno()).st_size
                    print("Pasta:", path, " | arquivos:", arquivos)
                    for file in arquivos:
                        file_path = os.path.join(BASE_DIR, subpath, file)
                        # print(path,file)
                        old_file = ArquivoRegistro.objects.filter(
                        name=file, id_usuario=user).last()
                        if file.endswith('.p7s'):
                            with open(file_path, 'rb') as s:
                                myfile.signature.save(file, File(s))
                                # myfile.save()
                        else:
                            myfile.name = file
                            myfile.shar256 = file_path_to_shar256(file_path)
                            with open(file_path, 'rb') as f:
                                myfile.file.save(file, File(f))
                                size = file_size(file_path)
                                if size > 0:
                                    myfile.size = size
                                if old_file:
                                    myfile.version = old_file.version + Decimal('1.0')
                        myfile.save()
                                
                    print("codregistro",registro[0].codregistro, "criou arquivo", registro[0].arquivo, 'file-pk', registro[0].arquivo.pk)
    print("\nArquivos exportados!")

# from tools.export_files import export
# BASE_DIR_EX = "/home/drummerzzz/workspace/python/teste"
# export(BASE_DIR_EX)