from cloudinary.models import CloudinaryField
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from instituicoes.models import Instituicoes
from avaliadores.models import Avaliadores
# from placer.models import Placer


class Instituicoes_Arquivos(models.Model):
    id_instituicao = models.ForeignKey(Instituicoes, on_delete=models.PROTECT)
    id_avaliador = models.ForeignKey(Avaliadores, on_delete=models.PROTECT)
    nome = models.CharField(max_length=100, default='')
    data_inicial = models.DateField(null=True, blank=True)
    data_final = models.DateField(null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    valor= models.DecimalField(max_digits=12, decimal_places=2, default=0)
    ativa = models.CharField(max_length=1, default='S', choices=False) # settings.ATIVO_CHOICES

    class Meta:
        ordering = ['-data_cadastro', ]

    def __str__(self):
        return  self.nome


# @receiver(post_save, sender=Instituicoes_Arquivos)
# def destivar_anuncios(sender, instance, **kwargs):
#    if instance.ativa == 'N':
#        anuncio = Anuncio.objects.filter(id_campanha__id=instance.id).update(ativo='N')


