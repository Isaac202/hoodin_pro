from _json import make_encoder
from django.contrib.auth import get_user_model
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from clientes.models import Clientes
from django.conf import settings

User = get_user_model()

class CompraTotalManager(models.Manager):
    def with_counts(self, data):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT SUM(compras_compras.valor), 
            COUNT(compras_compras.id) 
            FROM clientes_clientes, compras_compras
            WHERE clientes_clientes.id = compras_compras.id_cliente_id
            AND compras_compras.data = ?
            """, (data,))
            result_list = []
            for row in cursor.fetchall():
                # p = self.model(id=row[0], question=row[1], poll_date=row[2])
                # p.num_responses = row[3]
                p = {'total':row[0], 'quantidade':row[1] }
                result_list.append(p)
        return result_list


class CompraManager(models.Manager):
    def with_counts(self, data):
        total = 0;
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT clientes_clientes.nome, compras_compras.valor, 0 as total, clientes_clientes.cnpjcpf, 
            0 as quantidade, compras_compras.data, compras_compras.autorizado 
            FROM clientes_clientes, compras_compras
            WHERE clientes_clientes.id = compras_compras.id_cliente_id
            AND compras_compras.data = ? 
            group by clientes_clientes.nome, clientes_cli   entes.cnpjcpf, compras_compras.data,
            compras_compras.valor, compras_compras.autorizado
            order by compras_compras.data desc""", (data,))
            result_list = []
            for row in cursor.fetchall():
                # p = self.model(id=row[0], question=row[1], poll_date=row[2])
                # p.num_responses = row[3]
                total = total + row[1]
                p = {'cliente':row[0], 'valor':row[1], 'total':total, 'cnpjcpf':row[3], 'quantidade':row[4],  'data':row[5],  'autorizado':row[6] }
                result_list.append(p)
        return result_list


# Create your models here.
class Compras(models.Model):
    FORMA_PG_CHOICES = (
        ('Cartão de Crédito', 'Cartão de Crédito'),
        ('Cartão de Débito', 'Cartão de Débito'),
    )
    objects = CompraManager()

    id_usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    id_cliente = models.ForeignKey(Clientes, on_delete=models.PROTECT)
    valor = models.DecimalField(max_digits=11, decimal_places=2)
    data = models.DateTimeField(auto_now=True)
    forma_pagamento = models.CharField(max_length=30, default="Cartão de Crédito", choices=FORMA_PG_CHOICES)
    autorizado = models.BooleanField(default=False)
    codigo_compra_cielo = models.CharField(max_length=80, blank=True, null=True, default='0')
    transacao_cielo = models.CharField(max_length=80, blank=True, null=True)
    msg_cielo = models.CharField(max_length=150, blank=True, null=True)


    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'

# @receiver(post_save, sender=Compras)
# def autalizar_salado_cliente(sender, instance, **kwargs):
#     if instance.statu_trasacao == 'Transacao autorizada':
#         cli = Clientes.objects.filter(id_usuario=instance.id_cliente).first()
#         valor_atualizado = cli.valor_credito + instance.valor
#         Clientes.objects.filter(id_usuario=instance.id_cliente).update(valor_credito=valor_atualizado)


