from _json import make_encoder
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
# Create your models here.
class Codigos_Promocionais(models.Model):
    codpromocao=models.PositiveIntegerField(null=True, blank=True)
    promotor=models.CharField(max_length=255, null=True, blank=True)
    qrcode=models.CharField(max_length=255, null=True, blank=True)
    data_emissao=models.DateTimeField(auto_now=True)
    data_limite=models.DateTimeField(null=True, blank=True)
    data_resgate=models.DateTimeField(null=True, blank=True)
    cnpjcpf=models.CharField(max_length=18, null=True, blank=True)
    nome=models.CharField(max_length=255, null=True, blank=True)
    email=models.CharField(max_length=255, null=True, blank=True)
    tipo=models.CharField(max_length=1, null=True, blank=True)
    valor=models.DecimalField(max_digits=11,decimal_places=2, null=True, blank=True, default=0)
    id_cliente=models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Código promocional'
        verbose_name_plural = 'Códigos promocionais'

    def __str__(self):
        return self.nome

