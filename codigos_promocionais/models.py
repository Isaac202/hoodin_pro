from _json import make_encoder
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from servicos.models import Servicos
from tools.genereteKey import generate_hash_key
import time
# from django.utils import timezone


User = get_user_model()
# Create your models here.

Servicos

class Codigos_Promocionais(models.Model):
    codpromocao = models.PositiveIntegerField(null=True, blank=True)
    promotor = models.CharField(max_length=255, null=True, blank=True)
    qrcode = models.CharField(max_length=255, null=True, blank=True)
    data_emissao = models.DateTimeField(auto_now=True)
    data_limite = models.DateTimeField(null=True, blank=True)
    data_resgate = models.DateTimeField(null=True, blank=True)
    cnpjcpf = models.CharField(max_length=18, null=True, blank=True)
    nome = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    tipo = models.CharField(max_length=1, null=True, blank=True)
    valor = models.DecimalField(
        max_digits=11, decimal_places=2, null=True, blank=True, default=0)
    id_cliente = models.PositiveIntegerField(null=True, blank=True)
    resgate = models.BooleanField(default=False)
    id_servico = models.PositiveIntegerField(null=True, blank=True)

#    codservico = models.ForeignKey(Servicos, on_delete=models.PROTECT,
#                                      related_name='servico', verbose_name="informe servico")

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Código promocional'
        verbose_name_plural = 'Códigos promocionais'

    def __str__(self):
        return self.qrcode


class GeneratePromocionalCode(models.Model):
    quantidade = models.PositiveSmallIntegerField(default=1)
    data_inicio = models.DateField(
        "Data de inicio", auto_now=False, auto_now_add=False)
    valor = models.DecimalField(max_digits=11, decimal_places=2)
    data_fim = models.DateField(
        "Data de termino", auto_now=False, auto_now_add=False)
    nome = models.CharField(max_length=255, null=True, blank=True)
    cnpjcpf = models.CharField(max_length=18, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    tipo = models.CharField(max_length=1, null=True, blank=True)
    generated = models.BooleanField("gerado", default=False)
    id_servico = models.PositiveIntegerField(null=True, blank=True)

#    codservico = models.ForeignKey(Servicos, on_delete=models.PROTECT, null=True, blank=True,
#                                     related_name='servico', verbose_name="informe servico")

    class Meta:
        verbose_name = "Gerar código promocional"
        verbose_name_plural = "Gerar códigos promocionais"

    def __str__(self):
        return "{} x {}".format(self.quantidade, self.valor)


@receiver(pre_save, sender=GeneratePromocionalCode)
def create_promocional_codes(sender, instance, **kwargs):
    if not instance.generated:
        instance.generated = True
        for i in range(0, instance.quantidade):
            ts = time.time()
            salt = "Hoodid" + str(ts)
            hash_code = generate_hash_key(salt)
            Codigos_Promocionais.objects.create(
                # promotor=hash_code,
                qrcode=hash_code,
                data_emissao=instance.data_inicio,
                data_limite=instance.data_fim,
                cnpjcpf=instance.cnpjcpf,
                nome=instance.nome,
                email=instance.email,
                tipo=instance.tipo,
                valor=instance.valor,
                id_servico=instance.id_servico
            )
