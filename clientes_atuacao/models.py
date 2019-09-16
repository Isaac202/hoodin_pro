from _json import make_encoder
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
# Create your models here.
class Clientes_Atuacao(models.Model):
    codatuacao=models.PositiveIntegerField()
    codservico=models.PositiveIntegerField()
    codcliente=models.PositiveIntegerField()

