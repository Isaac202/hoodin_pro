from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from extensoes.models import Extensoes
from django.db.models.signals import post_save
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Servicos(models.Model):
    codservico =models.PositiveIntegerField(null=True, blank=True, default=0)
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    tamanho = models.PositiveIntegerField()
    medida = models.CharField(max_length=5, null=True, blank=True)
    servico_digitalizacao = models.BooleanField(default=False)
    extensoes = models.ManyToManyField(Extensoes, verbose_name="Extensoes serviçoes")
    
    class Meta:
        ordering = ('nome',)
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.nome


# class ServicosExtensoes(models.Model):
#     codservico = models.PositiveIntegerField() # models.ForeignKey(Servicos, on_delete=models.PROTECT, null=True)
#     codextensao = models.PositiveIntegerField()#OneToOneField(Extensoes,  on_delete=models.PROTECT, null=True,  blank= True, related_name='extensoes', verbose_name='Extensoes')
#         #models.ForeignKey(Extensoes, on_delete=models.PROTECT, null=True)