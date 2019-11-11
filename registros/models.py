from _json import make_encoder
from django.contrib.auth import get_user_model
from django.db import models
from servicos.models import Servicos
from clientes.models import Clientes


User = get_user_model()

class Registros(models.Model):
    codregistro = models.PositiveIntegerField(null=True)
    codcliente = models.ForeignKey(Clientes, on_delete=models.PROTECT, blank=True, null=True)
    codusuario = models.ForeignKey(User, on_delete=models.PROTECT)
    codservico = models.ForeignKey(Servicos, on_delete=models.PROTECT)
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    data = models.DateTimeField(auto_now=True)
    assinatura = models.FileField(blank=True, null=True)
    arquivo = models.FileField()
    versao = models.PositiveIntegerField()
    descricao = models.CharField(max_length=255)
    codqrcode = models.PositiveIntegerField(blank=True, null=True)
    codindicacao = models.PositiveIntegerField(blank=True, null=True)
    desconto = models.DecimalField(max_digits=9,decimal_places=2, default=0)
    resumo_obra = models.TextField(max_length=5000)



    class Meta:
        ordering = ('-data',)

    def __str__(self):
        return self.descricao

# Create your models here.
