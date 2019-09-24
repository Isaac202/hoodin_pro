from __future__ import absolute_import, unicode_literals
from celery import shared_task, task
from datetime import datetime
from decouple import config
import requests
import json

url_mandar_sms = config('SMS_URL_ENVIO')
url_gera_token_sms = config('URL_TOKEN_SMS')
client_id=config('CLIENT_ID_SMS')
client_secret=config('CLIENT_SECRET_SMS')
fone_origem = config('SMS_ORIGEM')


@shared_task
def pegar_token_sms():
    tk = ''
    try:
        data = {'client_id': client_id, 'client_secret': client_secret}
        token = requests.post(url_gera_token_sms, data=data)
        codigo_tk = token.json()
        if token.status_code == 200:
            tk = codigo_tk["access_token"]

    except Exception as e:
        print(e)

    return tk


@task
def enviar_sms(fone_destino, msg):

    caracters = "()-"

    for i in range(0, len(caracters)):
        fone_destino = fone_destino.replace(caracters[i],"")

    resultado = False
    tk =''
    try:
        tk = pegar_token_sms()
        fdestino ='55'+fone_destino
        data = {'origem': fone_origem, 'destino': fdestino, 'tipo':'texto', 'access_token':tk, 'texto':msg}
        envair =  requests.post(url_mandar_sms, data=data)
        resultado=True

    except Exception as e:
        print(e)
        resultado=False

    return resultado


