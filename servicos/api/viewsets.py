from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from servicos.models import Servicos
from .serializers import ServicoSerializer

from rest_framework.permissions import IsAuthenticated


class ServicoViewSet(ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Servicos.objects.all()
    serializer_class = ServicoSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome',)


