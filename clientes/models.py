from _json import make_encoder
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from configuracoes.tasks import enviar_sms
from django.conf import settings
from indicacoes.models import Indicacoes
from servicos.models import Servicos
from django.core.mail import send_mail
import json



User = get_user_model()


class Clientes(models.Model):
    codcliente = models.PositiveIntegerField(null=True, blank=True, default=0)
    nome = models.CharField(max_length=255)
    codusuario = models.OneToOneField(User, on_delete=models.PROTECT)
    email = models.EmailField(max_length=255, unique=True)
    valor_credito = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    telefone = models.CharField(max_length=16, null=True, blank=True)
    celular = models.CharField(max_length=16, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=1, default='', null=True, blank=True, choices=settings.SEXO_CHOICES)
    tipo_pessoa = models.CharField(max_length=1, null=True, blank=True, choices = settings.TIPOPESSOA_CHOICES)
    nome_mae = models.CharField(max_length=100, null=True, blank=True)
    nome_pai = models.CharField(max_length=100, null=True, blank=True)
    cnpjcpf = models.CharField(max_length=18, null=True, blank=True)
    #codindicacao = models.ForeignKey(Indicacoes,  on_delete = models.PROTECT, null = True,  blank = True,
    #                                    related_name='indicacao', verbose_name='Indicacao')
    senha = models.CharField(max_length=50)
    cep = models.CharField(max_length=9, null=True, blank=True)
    endereco = models.CharField(max_length=255, null=True, blank=True)
    complemento = models.CharField(max_length=255, null=True, blank=True)
    numero = models.CharField(max_length=8, null=True, blank=True)
    pais = models.CharField(max_length=50, null=True, blank=True, default='Brasil')
    estado = models.CharField(max_length=50, null=True, blank=True, default='PE', choices=settings.ESTADOS_CHOICES)
    cidade = models.CharField(max_length=50, null=True, blank=True)
    bairro = models.CharField(max_length=50, null=True, blank=True)
    documento_identidade = models.CharField(max_length=50, null=True, blank=True)
    documento_tipo = models.CharField(max_length=20, null=True, blank=True)
    passaporte = models.CharField(max_length=50, null=True, blank=True)
    nacionalidade = models.CharField(max_length=20, null=True, blank=True, default='Brasileiro')
    estadocivil = models.CharField(max_length=1, null=True, blank=True, choices=settings.ESTADO_CIVIL_CHOICES)
    biografia = models.TextField(max_length=5000, null=True, blank=True)
    nif = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    homepage = models.URLField(max_length=100, null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now=True)
    confirmation_key = models.CharField(max_length=80, default='0', blank=True, null=True)
    #atuacao = models.ManyToManyField(Servicos, blank=True, null=True)

    '''
    #
    codindicacao = models.PositiveIntegerField(null=True)
    
    area_pais = models.CharField(max_length=3, null=True, blank=True)
    identidade = models.CharField(max_length=20, null=True, blank=True)
    identidade_orgaoemissor = models.CharField(max_length=10, null=True, blank=True)
    codindicacao_cliente = models.PositiveIntegerField(null=True)
    
'''

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome



@receiver(pre_save, sender=Clientes)
def criar_usuario(sender, instance, **kwargs):

    conta = not User.objects.filter(username=instance.email).exists()

    if conta:
        usr = User.objects.create_user(
            username=instance.email,  email=instance.email,
            password=instance.senha, is_active=True)

        instance.codusuario = usr
        instance.confirmation_key = usr.confirmation_key


@receiver(post_save, sender=Clientes)
def sms_aviso(sender, instance, **kwargs):
    enviar_sms(instance.celular, 'Bem vindo a Hoodid Registros online')
    send_mail("Cadastro na Hoodid",
              'Usuário %s confirme seu email' + 'https://registrosonline.com.br/api/confirmar/?chave='
              + instance.confirmation_key + '&email=' + instance.email,
              settings.EMAIL_HOST_USER, [instance.email], fail_silently=True)


