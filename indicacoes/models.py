from django.db import models
from django.conf import settings
from datetime import datetime
# 'usuarios.User' = get_'usuarios.User'_model()


class Indicacoes(models.Model):
    codindicacao = models.PositiveIntegerField(null=True)
    nome = models.CharField(max_length=50)
    percentual_promocional = models.DecimalField(max_length=9, decimal_places=2)

    class Meta:
        ordering = ['nome', ]

    def __str__(self):
        return self.nome
