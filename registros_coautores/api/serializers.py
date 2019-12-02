from rest_framework.serializers import ModelSerializer
from registros_coautores.models import Coautores
from registros.api.serializers import ArquivoSerializer

class CoautorSerializer(ModelSerializer):
    
    arquivo = ArquivoSerializer(many=False, read_only=True)
    
    class Meta:
        model = Coautores
        fields = "__all__"