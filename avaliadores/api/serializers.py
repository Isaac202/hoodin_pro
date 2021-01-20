from rest_framework.serializers import ModelSerializer
from avaliadores.models import Avaliadores


class AvaliadoresSerializer(ModelSerializer):
    class Meta:
        model = Avaliadores
        fields = ['id', 'nome', 'perfil', 'cnpj', 'data_cadastro']


