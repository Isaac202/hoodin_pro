from _json import make_encoder
from django.db import models

# Create your models here.
class Servicos_Extensoes(models.Model):
    codservicoext=models.PositiveIntegerField()
    codservico=models.PositiveIntegerField()
    codextensao=models.PositiveIntegerField()

