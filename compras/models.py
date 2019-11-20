from _json import make_encoder
from django.contrib.auth import get_user_model
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from clientes.models import Clientes
from django.conf import settings

User = get_user_model()


# Create your models here.
class Compras(models.Model):
    FORMA_PG_CHOICES = (
        ('Cartão de Crédito', 'Cartão de Crédito'),
        ('Cartão de Débito', 'Cartão de Débito'),
    )

    id_usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    id_cliente = models.ForeignKey(Clientes, on_delete=models.PROTECT)
    valor = models.DecimalField(max_digits=11, decimal_places=2)
    data = models.DateTimeField(auto_now=True)
    forma_pagamento = models.CharField(max_length=30, choices=FORMA_PG_CHOICES)
    autorizado = models.BooleanField(default=False)
    codigo_compra_cielo = models.CharField(max_length=80, blank=True, null=True, default='0')
    transacao_cielo = models.CharField(max_length=80, blank=True, null=True)
    msg_cielo = models.CharField(max_length=150, blank=True, null=True)




@receiver(post_save, sender=Compras)
def autalizar_salado_cliente(sender, instance, **kwargs):
    if instance.statu_trasacao == 'Transacao autorizada':
        cli = Clientes.objects.filter(id_usuario=instance.id_cliente).first()
        valor_atualizado = cli.valor_credito + instance.valor
        Clientes.objects.filter(id_usuario=instance.id_cliente).update(valor_credito=valor_atualizado)


