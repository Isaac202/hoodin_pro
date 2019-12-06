from rest_framework.serializers import ModelSerializer
from registros.models import ArquivoRegistro


class ArquivoSerializer(ModelSerializer):
    class Meta:
        model = ArquivoRegistro
        exclude = ('paid', 'update_at', 'id_usuario', 'shar256',
                   'create_at', 'signature', 'size')
