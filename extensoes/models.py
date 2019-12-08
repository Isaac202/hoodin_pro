from _json import make_encoder
from django.db import models
# Create your models here.


class Extensoes(models.Model):
    codextensao = models.PositiveIntegerField(null=True, blank=True, default=0)
    nome = models.CharField(max_length=5, unique=True)

    class Meta:
        ordering = ['nome', ]
        verbose_name = 'Extesão'
        verbose_name_plural = 'Extensões'

    def __str__(self):
        return self.nome
