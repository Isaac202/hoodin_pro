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
    cep=models.CharField(max_length=9)

    '''
    endereco
    complemento
    numero
    pais
    estado
    cidade
    bairro
    telefone
    celular
    tipo_pessoa
    area_pais
    nome_mae
    nome_pai
    identidade
    identidade_orgaoemissor
    banco_1
    agencia_1
    contacorrente_1
    banco_2
    agencia_2
    contacorrente_2
    sexo
    cnpjcpf
    checki
    checkival
    passaporte
    nacionalidade
    estadocivil
    mail
    biografia
    codindicacao
    nif
    codindicacao_cliente
    documento_identidade
    documento_tipo
    facebook
    twitter
    homepage
    '''

# Create your models here.
