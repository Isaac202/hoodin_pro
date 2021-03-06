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
from tools.genereteKey import generate_hash_key
from codigos_promocionais.utils import set_codigo_promocional
from datetime import datetime
from django_countries.fields import CountryField

User = get_user_model()

TIPO_DOCUMENTO = (
    ('RG', 'RG'),
    ('CNH', 'CNH'),
    ('Seguro Social', 'Seguro Social'),
    ('Titulo de Eleitor', 'Titulo de Eleitor'),
    ('Conselho de Classe', 'Conselho de Classe'),
    ('Outros', 'Outros'),
    ('NIF', 'NIF'),
)

Indicacoes


class Clientes(models.Model):
    id_usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    id_cliente = models.PositiveIntegerField(null=True, blank=True, default=0)
    nome = models.CharField(max_length=255)
    # email = models.EmailField(max_length=255, unique=True)
    valor_credito = models.DecimalField(
        max_digits=11, decimal_places=2, default=0)
    pontuacao = models.DecimalField(
        max_digits=11, decimal_places=2, default=0)
    telefone = models.CharField(
        "Telefone Fixo", max_length=16, null=True, blank=True)
    celular = models.CharField("Celular *", max_length=16)
    data_nascimento = models.DateField("Data de nascimento *")
    sexo = models.CharField("Sexo *", max_length=1,
                            choices=settings.SEXO_CHOICES, blank=True, null=True)
    tipo_pessoa = models.CharField(
        "Tipo de Pessoa *", max_length=1, default="F", choices=settings.TIPOPESSOA_CHOICES)
    nome_mae = models.CharField(
        "Nome da Mãe", max_length=100, null=True, blank=True)
    nome_pai = models.CharField(
        "Nome do Pai", max_length=100, null=True, blank=True)
    cnpjcpf = models.CharField("CPF/CNPJ ", max_length=18, blank=True)
    codindicacao = models.ForeignKey(Indicacoes, on_delete=models.PROTECT,
                                     related_name='indicacao', verbose_name="Como conheceu a Hoodid.com? *")
    cep = models.CharField("Cep *", max_length=9)
    endereco = models.CharField("Endereço *", max_length=255)
    complemento = models.CharField(
        "Complemento", max_length=255, null=True, blank=True)
    numero = models.CharField("Número *", max_length=8)
    pais = CountryField(default='BR')
    #estado = models.CharField("Estado *", max_length=50, default='PE',
    #                          choices=settings.ESTADOS_CHOICES)
    estado = models.CharField("Estado *", max_length=50)
    cidade = models.CharField("Cidade *", max_length=50)
    bairro = models.CharField("Bairro *", max_length=50)
    documento_identidade = models.CharField(
        "Número do Documento de Identificação *", max_length=50, blank=True, null=True)
    documento_tipo = models.CharField(
        "Tipo de Documento de Identificação *", max_length=20, choices=TIPO_DOCUMENTO, blank=True, null=True)
    passaporte = models.CharField(max_length=50, null=True, blank=True)
    nacionalidade = models.CharField(
        "Nacionalidade *", max_length=20, default='')
    estadocivil = models.CharField("Estado civil *", 
                max_length=1, choices=settings.ESTADO_CIVIL_CHOICES, blank=True, null=True)
    biografia = models.TextField(max_length=5000, null=True, blank=True)
    nif = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    homepage = models.CharField(max_length=100, null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    confirmation_key = models.CharField(
        max_length=80, default='0', blank=True, null=True)
    atuacao = models.ManyToManyField(
        Servicos, verbose_name="AREA DE INTERESSE", blank=True)
    codigo_promocional = models.CharField(
        "Codigo Promocional", max_length=200, blank=True, null=True)
    link_indicacao = models.CharField(
        "Link de Indicação", max_length=200, blank=True, null=True)
    meu_link_indicacao = models.CharField(
        "Meu link de Indicação", max_length=200, blank=True, null=True)

    class Meta:
        ordering = ('nome',)
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nome

    def get_sexo(self): 
        if self.is_cpf():
            sexo = self.sexo
            for s in settings.SEXO_CHOICES:
                if s[0] in sexo:
                    return s[1]
        return "-----"

    def get_estadocivil(self):
        if self.is_cpf():
            esc = self.estadocivil
            for s in settings.ESTADO_CIVIL_CHOICES:
                if s[0] in esc:
                    return s[1]
        return "-----"

    def is_cpf(self):
        if len(self.cnpjcpf) > 14:
            return False
        return True

    def get_credit(self):
        return "%.2f" % self.valor_credito


@receiver(pre_save, sender=Clientes)
def type_person(sender, instance, **kwargs):
    if not instance.is_cpf:
        instance.tipo_pessoa = "J"
    if instance.meu_link_indicacao in [None, '']:
        instance.meu_link_indicacao = generate_hash_key(
            instance.id_usuario.username, 3)
    codigo = instance.codigo_promocional
    if codigo:
        promocao = set_codigo_promocional(codigo, instance)
        if promocao:
            instance.valor_credito += promocao.valor
    instance.codigo_promocional = ""


@receiver(post_save, sender=Clientes)
def sms_aviso(sender, instance, created, **kwargs):
    if created:
        enviar_sms(instance.celular, 'Bem vindo a Hoodid Registros online')
