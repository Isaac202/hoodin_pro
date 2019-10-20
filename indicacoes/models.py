from django.db import models
from django.conf import settings
from datetime import datetime
# 'usuarios.User' = get_'usuarios.User'_model()


class Indicacao(models.Model):
    code_bisavo = models.CharField(
        "Codigo do Bisavó", max_length=100, blank=True, null=True)
    code_avo = models.CharField(
        "Codigo do Avó", max_length=100, blank=True, null=True)
    code_pai = models.CharField("Codigo do Pai", max_length=100)
    filho = models.ForeignKey(
        'usuarios.User', verbose_name='cliente', on_delete=models.CASCADE)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-data_cadastro',)


class IndicadoPor(models.Model):
    nome = models.CharField(max_length=80, unique=True)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome
