from django.db import models
from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Servicos(models.Model):
    codservico=models.PositiveIntegerField()
    nome=models.CharField(max_length=100)
    preco=models.DecimalField(max_digits=11,decimal_places=2)
    tamanho=models.PositiveIntegerField()
    medida=models.CharField(max_length=5)
    servico_digitalizacao=models.CharField(max_length=1)
