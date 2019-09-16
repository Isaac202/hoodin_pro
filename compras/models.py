from _json import make_encoder
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
# Create your models here.
class Compras(models.Model):
    codcompra=models.PositiveIntegerField()
    codcliente=models.PositiveIntegerField()
    valor=models.DecimalField(max_digits=11,decimal_places=2)
    data=models.DateTimeField(auto_now=True)
    formapagamento=models.CharField(max_length=10)
    autorizado=models.CharField(max_length=1)


