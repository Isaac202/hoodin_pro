from __future__ import absolute_import, unicode_literals
from decimal import *
from celery import shared_task, task
import hashlib
from registros.models import Registros


@task
def extrair_has(usuario):
    arqu_usr = Registros.objects.filter(codcliente=usuario).frist()
    arquivo = arqu_usr.arquivo
    BLOCK_SIZE = 85536  # The size of each read from the file

    arquivo_hash = hashlib.sha256()  # Create the hash object, can use something other than `.sha256()` if you wish
    with open(arquivo, 'rb') as f:  # Open the file to read it's bytes
        fb = f.read(BLOCK_SIZE)  # Read from the file. Take in the amount declared above
        while len(fb) > 0:  # While there is still data being read from the file
            arquivo_hash.update(fb)  # Update the hash
            fb = f.read(BLOCK_SIZE)  # Read the next block from the file

    return  arquivo_hash.hexdigest()


@task
def enviar_arqivo_para_bry(usuario):
    has_usr = Registros.objects.filter(codcliente=usuario).frist()
    #TODO ENVAIR PARA BRY
