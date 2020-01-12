from django.core.mail import send_mail
from twilio.rest import Client
import logging

loogger = logging.getLogger('otica_error')

def enviar_email(titulo, msg, de, para):
    try:
         send_mail(titulo, msg, de, [para], fail_silently=False)
         return 'ok'
    except Exception as e:
        loogger.error('erro task enviar email' + str(e))
        enviar_notificacao(str(e))
        return 'deu merda'

def enviar_notificacao(msg):
    account_sid = "AC2601d12123d4a71566381fe0a2140cb4"
    auth_token = "f99b19ed0ef07c8f5d766007eaa8288f"
    client = Client(account_sid, auth_token)
    try:
        message = client.messages.create(
            body=msg,
            to="+5587999250141",  # remplazamos con nuestro numero o al que queramos enviar el sms
            from_="+118596666080")  # el numero que nos asigno twilio
        message.sid
        return "notificacao_enviada"
    except Exception as e:
        return str(e)



def remove_exention_file(name):
    name = name.split('.')[:-1] 
    name = ' '.join(map(str, name))
    return name