from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from clientes.models import Clientes


class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Clientes
        fields = ['id', 'codcliente',  'nome', 'codusuario', 'email', 'valor_credito', 'telefone', 'celular',
                  'data_nascimento', 'sexo', 'tipo_pessoa', 'nome_mae', 'nome_pai', 'cnpjcpf', 'codindicacao', 'senha',
                  'cep', 'endereco', 'bairro', 'complemento', 'numero', 'pais', 'estado', 'cidade',
                  'documento_identidade', 'documento_tipo', 'passaporte',  'nacionalidade', 'estadocivil', 'biografia',
                  'biografia', 'nif', 'facebook', 'twitter', 'homepage', 'data_cadastro']

        read_only_fields = ['codusuario']


