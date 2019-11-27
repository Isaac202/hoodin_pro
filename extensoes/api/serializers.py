from rest_framework.serializers import ModelSerializer
from extensoes.models import Extensoes


class ExentsaoSerializer(ModelSerializer):
    class Meta:
        model = Extensoes
        fields = ['id', 'nome']
