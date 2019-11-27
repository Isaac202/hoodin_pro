from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from servicos.models import Servicos
from extensoes.api.serializers import ExentsaoSerializer

class ServicoSerializer(ModelSerializer):
    class Meta:
        model = Servicos
        fields = ['id','nome', 'preco', 'tamanho', 'medida', 'servico_digitalizacao']

        read_only_fields = ['codservico']



class ServiceExtentionSerializer(ModelSerializer):
    
    extensoes = ExentsaoSerializer(read_only=True, many=True)

    class Meta:
        model = Servicos
        fields = ['id','nome', 'preco', 'tamanho', 'medida', 'servico_digitalizacao','extensoes']
        read_only_fields = ['codservico']

