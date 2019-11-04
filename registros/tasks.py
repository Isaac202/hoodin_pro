from __future__ import absolute_import, unicode_literals
from celery import shared_task, task
from datetime import datetime
from decouple import config
import json
from cieloApi3 import *
import requests
from django.contrib.auth import get_user_model
import hashlib
import logging
User = get_user_model()




def extrair_has(arquivo):
    BLOCK_SIZE = 65536
    file_hash = hashlib.sha256()
    try:
        with open(arquivo, 'rb') as f:  # Open the file to read it's bytes
            fb = f.read(BLOCK_SIZE)  # Read from the file. Take in the amount declared above
            while len(fb) > 0:  # While there is still data being read from the file
                file_hash.update(fb)  # Update the hash
                fb = f.read(BLOCK_SIZE)  # Read the next block from the file

        return file_hash.hexdigest()


    except Exception as e:

        return str(e)


@task
def enviar_para_bry(has_file):
    pegar_hash = extrair_has(has_file)
    pass






