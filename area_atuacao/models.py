from _json import make_encoder
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

# Create your models here.
class Area_Atuacao(models.Model):
    #codextensao=models.PositiveIntegerField()
    nome = models.CharField(max_length=20)
    texto = models.CharField(max_length=2500)

    class Meta:
        ordering = ['nome', ]

    def __str__(self):
        return self.nome
