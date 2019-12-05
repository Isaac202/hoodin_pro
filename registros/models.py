from _json import make_encoder
from django.contrib.auth import get_user_model
from django.db import models
from servicos.models import Servicos
from clientes.models import Clientes
from datetime import date

User = get_user_model()

def user_directory_path(instance, filename):
    return 'registros/{}/{}/{}'.format(instance.id_usuario.username, date.today(), filename)



class ArquivoRegistro(models.Model):
    id_usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=250)
    size = models.PositiveIntegerField()
    shar256 = models.CharField(max_length=90)
    file = models.FileField(upload_to=user_directory_path)
    signature = models.FileField(blank=True, null=True, upload_to=user_directory_path)
    version = models.DecimalField(max_digits=9,decimal_places=2, default=1.0)
    paid = models.BooleanField(default=False)
    resume = models.TextField(max_length=5000, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Registros(models.Model):
    codregistro = models.PositiveIntegerField(blank=True, null=True)
    id_usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    id_cliente = models.ForeignKey(Clientes, on_delete=models.PROTECT, blank=True, null=True)
    codservico = models.ForeignKey(Servicos, verbose_name="Serviço", on_delete=models.PROTECT)
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    data = models.DateTimeField(auto_now=True)
    arquivo = models.OneToOneField(ArquivoRegistro, verbose_name="arquivo", on_delete=models.CASCADE)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    codqrcode = models.PositiveIntegerField(blank=True, null=True)
    codindicacao = models.PositiveIntegerField("Código de indicação", blank=True, null=True)
    desconto = models.DecimalField(max_digits=9,decimal_places=2, default=0)
    codigo_promocional = models.CharField("Codigo Promocional", max_length=200, blank=True, null=True)


    class Meta:
        ordering = ('-data',)

    def __str__(self):
        return self.descricao

# Create your models here.

