from _json import make_encoder
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
# Create your models here.
class Codigos_Promocionais(models.Model):
    codpromocao=models.PositiveIntegerField(null=True)
    promotor=models.CharField(max_length=255)
    qrcode=models.CharField(max_length=255)
    data_emissao=models.DateTimeField(auto_now=True)
    data_limite=models.DateTimeField()
    data_resgate=models.DateTimeField()
    cnpjcpf=models.CharField(max_length=18)
    nome=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    tipo=models.CharField(max_length=1)
    valor=models.DecimalField(max_digits=11,decimal_places=2)
    codcliente=models.PositiveIntegerField()


