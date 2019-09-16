from _json import make_encoder
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
class Clientes(models.Model):
    #padrão é não nulo
    codcliente=models.PositiveIntegerField()
    nome=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    codusuario=models.OneToOneField(User, on_delete=models.PROTECT)
    valor_credito=models.DecimalField(max_digits=11,decimal_places=2)
    data_cadastro=models.DateTimeField(auto_now=True)
    data_nascimento=models.DateField()
    cep=models.CharField(max_length=9, null=True, blank=True)
    endereco=models.CharField(max_length=255, null=True, blank=True)
    complemento=models.CharField(max_length=255, null=True, blank=True)
    numero=models.CharField(max_length=8, null=True, blank=True)
    pais=models.CharField(max_length=50, null=True, blank=True)
    estado=models.CharField(max_length=50, null=True, blank=True)
    cidade=models.CharField(max_length=50, null=True, blank=True)
    bairro=models.CharField(max_length=50, null=True, blank=True)
    telefone=models.CharField(max_length=16, null=True, blank=True)
    celular=models.CharField(max_length=16, null=True, blank=True)
    tipo_pessoa=models.CharField(max_length=1, null=True, blank=True)
    area_pais=models.CharField(max_length=3, null=True, blank=True)
    nome_mae=models.CharField(max_length=100, null=True, blank=True)
    nome_pai=models.CharField(max_length=100, null=True, blank=True)
    identidade=models.CharField(max_length=20, null=True, blank=True)
    identidade_orgaoemissor=models.CharField(max_length=10, null=True, blank=True)
    sexo=models.CharField(max_length=1, null=True, blank=True)
    cnpjcpf=models.CharField(max_length=18, null=True, blank=True)
    passaporte=models.CharField(max_length=50, null=True, blank=True)
    nacionalidade=models.CharField(max_length=20, null=True, blank=True)
    estadocivil=models.CharField(max_length=1, null=True, blank=True)
    biografia=models.CharField(max_length=5000, null=True, blank=True)
    codindicacao=models.PositiveIntegerField(null=True)
    nif=models.CharField(max_length=100, null=True, blank=True)
    codindicacao_cliente=models.PositiveIntegerField(null=True)
    documento_identidade=models.CharField(max_length=50, null=True, blank=True)
    documento_tipo=models.CharField(max_length=20, null=True, blank=True)
    facebook=models.CharField(max_length=100, null=True, blank=True)
    twitter=models.CharField(max_length=100, null=True, blank=True)
    homepage=models.CharField(max_length=100, null=True, blank=True)
'''
comentário
'''
# Create your models here.
