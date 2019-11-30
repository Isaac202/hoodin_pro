from _json import make_encoder
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
# Create your models here.
class Registros_Coautores(models.Model):
    codcoautor = models.PositiveIntegerField(null=True)
    codregistro = models.PositiveIntegerField()
    nome = models.CharField(max_length=255)
    documento = models.CharField(max_length=100)
    percentual_obra = models.DecimalField(max_length=5,decimal_places=2)


class Coautores(models.Model):
    nome = models.CharField(max_length=255)
    documento = models.ForeignKey("registros.ArquivoRegistro", verbose_name="Arquivo", on_delete=models.CASCADE)
    percentual_obra = models.DecimalField(max_length=5,decimal_places=2)
