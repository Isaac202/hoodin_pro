from _json import make_encoder
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
# Create your models here.
class Precos(models.Model):
    codservico=models.PositiveIntegerField()
    valor=models.DecimalField(max_digits=11,decimal_places=2)
    tipo_servico=models.CharField(max_length=1)

