from __future__ import absolute_import, unicode_literals
from celery import shared_task, task
from hoodid.celery import app
from tools.mail import send_mail_template
import requests
import json
import logging
# from datetime import datetime
from decouple import config
# from django.contrib.auth.hashers import check_password
# from django.core.mail import send_mail

loogger = logging.getLogger('tarefa_erro')

@app.task
def send_mail(subject, template_name, context, recipient_list):
    return send_mail_template(subject, template_name, context, recipient_list)


@app.task
def teste():
    print("testando celery\n\n\n")