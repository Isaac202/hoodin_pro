from _json import make_encoder
from django.contrib.auth import get_user_model
from django.db import models
from area_atuacao.models import Area_Atuacao
from servicos.models import Servicos

User = get_user_model()
# Create your models here.
class Clientes_Atuacao(models.Model):
    codcliente = models.ForeignKey(User, on_delete=models.PROTECT)
    codatuacao=models.ForeignKey(Area_Atuacao, on_delete=models.PROTECT, verbose_name='Área de Interesse')
    codservico=models.ForeignKey(Servicos, on_delete=models.PROTECT, verbose_name='Serviço')


