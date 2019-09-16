from _json import make_encoder
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
# Create your models here.
class Servicos_Extensoes(models.Model):
    codservicoext=models.PositiveIntegerField()
    codservico=models.PositiveIntegerField()
    codextensao=models.PositiveIntegerField()

