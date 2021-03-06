from _json import make_encoder
from django.contrib.auth import get_user_model
from django.db import models
from servicos.models import Servicos
from clientes.models import Clientes
from datetime import date
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import datetime

User = get_user_model()


def user_directory_path(instance, filename):
    return 'registros/{}/{}/{}'.format(instance.id_usuario.username, date.today(), filename)

def set_code_registro(pk):
    today = datetime.now()
    code = '{}{}{}{}'.format(today.day, today.second, pk, today.microsecond)
    return code


class ArquivoRegistro(models.Model):
    id_usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    code = models.CharField("Codigo deo registro", max_length=100, blank=True, null=True)
    name = models.CharField(max_length=250)
    content_type = models.CharField('content_type', max_length=50, blank=True, null=True)
    size = models.PositiveIntegerField(default=1)
    b64 = models.TextField(blank=True, null=True)
    file = models.FileField(
        upload_to=user_directory_path, blank=True, null=True)
    signature = models.FileField(
        blank=True, null=True, upload_to=user_directory_path)
    version = models.DecimalField(max_digits=9, decimal_places=2, default=1.0)
    paid = models.BooleanField(default=False)
    value = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    resume = models.TextField(max_length=5000, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    codregistro = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "Arquivo"
        verbose_name_plural = "Arquivos"

    def __str__(self):
        return self.name


@receiver(pre_save, sender=ArquivoRegistro)
def my_callback(sender, instance, *args, **kwargs):
    if instance.resume in [None, ""]:
        name = instance.name.split('.')[:-1]
        name = ' '.join(map(str, name))
        instance.resume = name


class RegistroManager(models.Manager):
    def with_counts(self):
        valor_total = 0
        quantidade_total = 0;
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT clientes_clientes.nome, servicos_servicos.nome, SUM(registros_registros.valor), 
            COUNT(registros_registros.id), clientes_clientes.celular, usuarios_user.email, 
            0 as valoracumulado, 0 as quantidadeacumulado 
            FROM clientes_clientes, servicos_servicos, registros_registros, usuarios_user
            WHERE clientes_clientes.id = registros_registros.id_cliente_id
            AND usuarios_user.id = clientes_clientes.id_usuario_id
            AND registros_registros.codservico_id = servicos_servicos.id
            group by clientes_clientes.nome, servicos_servicos.nome, clientes_clientes.celular, usuarios_user.email
            order by clientes_clientes.nome""")
            result_list = []
            for row in cursor.fetchall():
                # p = self.model(id=row[0], question=row[1], poll_date=row[2])
                # p.num_responses = row[3]
                valor_total = valor_total + row[2]
                quantidade_total = quantidade_total + row[3]
                p = {'cliente':row[0], 'servico':row[1], 'valor':row[2], 'quantidade':row[3], 'celular':row[4], 'email':row[5],
                     'valoracumulado':valor_total, 'quantidadeacumulado':quantidade_total }
                result_list.append(p)
        return result_list


class Registros(models.Model):
    
    objects = RegistroManager()

    codregistro = models.PositiveIntegerField(blank=True, null=True)
    id_usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    id_cliente = models.ForeignKey(
        Clientes, on_delete=models.PROTECT, blank=True, null=True)
    codservico = models.ForeignKey(
        Servicos, verbose_name="Servi??o", on_delete=models.PROTECT)
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    data = models.DateTimeField(auto_now=True)
    arquivo = models.OneToOneField(
        ArquivoRegistro, verbose_name="arquivo", on_delete=models.CASCADE, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    codqrcode = models.PositiveIntegerField(blank=True, null=True)
    desconto = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    codigo_promocional = models.CharField(
        "Codigo Promocional", max_length=200, blank=True, null=True)
    manter_arquivo = models.BooleanField(default=True)
    excluido = models.BooleanField(default=False)

    class Meta:
        ordering = ('-data',)
        verbose_name = "Registro"
        verbose_name_plural = "Registros"

    def __str__(self):
        return self.arquivo.name

# Create your models here.
