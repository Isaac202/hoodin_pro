from _json import make_encoder
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
# Create your models here.
class Compras(models.Model):
    codcliente = models.ForeignKey(User, on_delete=models.PROTECT)
    valor = models.DecimalField(max_digits=11,decimal_places=2)
    data = models.DateTimeField(auto_now=True)
    forma_pagamento = models.CharField(max_length=10)
    autorizado = models.BooleanField(max_length=1)
    codigo_compra_cielo = models.CharField(max_length=80, blank=True, null=True, default='0')
    transacao_cielo = models.CharField(max_length=80, blank=True, null=True)
    msg_cielo = models.CharField(max_length=150, blank=True, null=True)


