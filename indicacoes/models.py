from _json import make_encoder
from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()
class Indicacoes(models.Model):
    codindicacao=models.AutoField(primary_key=True)
    nome=models.CharField(max_length=100)
   # percentual_promocional=models.DecimalField(max_digits=5,decimal_places=2)
    



# Create your models here.
