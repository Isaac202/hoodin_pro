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
from datetime import datetime

User = get_user_model()


class Clientes(models.Model):
    id_usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    id_cliente = models.PositiveIntegerField(null=True, blank=True, default=0)
    nome = models.CharField(max_length=255)
    # email = models.EmailField(max_length=255, unique=True)
    valor_credito = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    telefone = models.CharField("Telefone Fixo",max_length=16, null=True, blank=True)
    celular = models.CharField("Celular *", max_length=16)
    data_nascimento = models.DateField("Data de nascimento *")
    sexo = models.CharField("Sexo *", max_length=1, choices=settings.SEXO_CHOICES)
    tipo_pessoa = models.CharField("Tipo de Pessoa *", max_length=1, default="F", choices=settings.TIPOPESSOA_CHOICES)
    nome_mae = models.CharField("Nome da Mãe",max_length=100, null=True, blank=True)
    nome_pai = models.CharField("Nome do Pai", max_length=100, null=True, blank=True)
    cnpjcpf = models.CharField("CPF/CNPJ *", max_length=18)
    codindicacao = models.ForeignKey(Indicacoes, on_delete = models.PROTECT, 
                related_name='indicacao', verbose_name="Como conheceu a gente? *")
    cep = models.CharField("Cep *", max_length=9)
    endereco = models.CharField("Endereço *", max_length=255)
    complemento = models.CharField("Complemento", max_length=255, null=True, blank=True)
    numero = models.CharField("Número *", max_length=8)
    pais = models.CharField("País de Origem *", max_length=50, default='Brasil')
    estado = models.CharField("Estado *", max_length=50, default='PE', 
                            choices=settings.ESTADOS_CHOICES)
    cidade = models.CharField("Cidade *", max_length=50)
    bairro = models.CharField("Bairro *", max_length=50)
    documento_identidade = models.CharField("Documento de identificação *", max_length=50)
    documento_tipo = models.CharField("Tipo de Documento *", max_length=20)
    passaporte = models.CharField(max_length=50, null=True, blank=True)
    nacionalidade = models.CharField("Nacionalidade *", max_length=20, default='Brasileiro')
    estadocivil = models.CharField("Estado civil *",max_length=1, choices=settings.ESTADO_CIVIL_CHOICES)
    biografia = models.TextField(max_length=5000, null=True, blank=True)
    nif = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    homepage = models.URLField(max_length=100, null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    confirmation_key = models.CharField(max_length=80, default='0', blank=True, null=True)
    atuacao = models.ManyToManyField(Servicos, blank=True)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome


    def is_cpf(self):
        if len(self.cnpjcpf) > 14: 
            return False
        return True

    # def save(self, *args,**kwargs):
    #     super(Clientes, self).save(*args, **kwargs)
    #     try:

    #         send_mail("Cadastro na Hoodid",
    #               'Usuário %s confirme seu email' + 'https://registrosonline.com.br/api/confirmar/?chave='
    #               + self.confirmation_key + '&email=' + self.email, settings.EMAIL_HOST_USER,
    #               [ self.email], fail_silently=True)
    #     except Exception as e:
    #         print(str(e))


# @receiver(pre_save, sender=Clientes)
# def criar_usuario(sender, instance, **kwargs):

#     conta = not User.objects.filter(username=instance.email).exists()

#     if conta:
#         usr = User.objects.create_user(
#             username=instance.email,  email=instance.email,
#             password=instance.senha, is_active=True)
#         agora = datetime.now()


#         instance.id_usuario = usr
#         instance.confirmation_key = str(usr.id) + str((10000*agora.year + 100*agora.month + agora.day))


@receiver(pre_save, sender=Clientes)
def type_person(sender, instance, **kwargs):
    if not instance.is_cpf:
        instance.tipo_pessoa = "J"


@receiver(post_save, sender=Clientes)
def sms_aviso(sender, instance, **kwargs):
    enviar_sms(instance.celular, 'Bem vindo a Hoodid Registros online')


 


