from django.db import models
from django.conf import settings
from datetime import datetime
# 'usuarios.User' = get_'usuarios.User'_model()


class Indicacoes(models.Model):
    codindicacao = models.PositiveIntegerField(
        null=True, blank=True, default=0)
    nome = models.CharField(max_length=50)
    percentual_promocional = models.DecimalField(
        max_digits=11, decimal_places=2, null=True, blank=True,  default=0)

    class Meta:
        ordering = ['nome', ]
        verbose_name = 'Indicação'
        verbose_name_plural = 'Indicações'

    def __str__(self):
        return self.nome



class IndicacaoCliente(models.Model):
    email_pai = models.EmailField()
    email_filho = models.EmailField()
    code_pai = models.CharField(max_length=200)
    code_filho = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Indicação Cliente"
        verbose_name_plural = "Indicações Clientes"

    def __str__(self):
        return self.code_pai

    # def get_absolute_url(self):
    #     return reverse("IncicacaoCliente_detail", kwargs={"pk": self.pk})
