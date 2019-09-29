from _json import make_encoder
from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings
from servicos.models import Servicos

User = get_user_model()
# Create your models here.
class Precos(models.Model):
    codservico = models.OneToOneField(Servicos,  on_delete=models.PROTECT, null=True, related_name='servico', verbose_name='Servico')
    valor = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    tipo_servico = models.CharField(max_length=1, null=True, blank=True)

