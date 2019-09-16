from _json import make_encoder
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
class Registros(models.Model):
    codregistro=models.PositiveIntegerField()
    codcliente=models.PositiveIntegerField()
    codservico=models.PositiveIntegerField()
    valor=models.DecimalField(max_digits=9,decimal_places=2)
    data=models.DateTimeField(auto_now=True)
    caminho_arquivo=models.CharField(max_length=255)
    assinatura=models.BinaryField()
    versao=models.PositiveIntegerField()
    descricao=models.CharField(max_length=255)
    codqrcode=models.PositiveIntegerField()
    codindicacao=models.PositiveIntegerField()
    desconto=models.DecimalField(max_digits=9,decimal_places=2)
    resumo_obra=models.CharField(max_length=5000)

# Create your models here.
