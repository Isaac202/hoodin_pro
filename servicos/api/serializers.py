from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from servicos.models import Servicos


class ServicoSerializer(ModelSerializer):
    class Meta:
        model = Servicos
        fields = ['id','nome', 'preco', 'tamanho', 'medida', 'servico_digitalizacao']

        read_only_fields = ['codservico']


