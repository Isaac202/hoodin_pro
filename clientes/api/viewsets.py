from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from clientes.models import Clientes
from .serializers import ClienteSerializer

from rest_framework.permissions import IsAuthenticated


class ClienteViewSet(ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Clientes.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'email')
    lookup_field = 'id_usuario'

