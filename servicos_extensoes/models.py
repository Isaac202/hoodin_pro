from _json import make_encoder
from django.db import models
from servicos.models import Servicos
from extensoes.models import Extensoes


# Create your models here.
class Servicos_Extensoes(models.Model):
    codservico = models.ForeignKey(Servicos, on_delete=models.PROTECT)
    codextensao = models.ForeignKey(Extensoes, on_delete=models.PROTECT)

    def __str__(self):
        return self.codservico, self.codextensao