from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from campanha.models import Campanha, Anuncio
from .serializers import CampanhaSerializer, AnuncioSerializer
from datetime import datetime


class CampanhaViewSet(ModelViewSet):
    queryset = Campanha.objects.filter(ativa='S', data_final__gte=datetime.now())
    serializer_class = CampanhaSerializer


class AnuncioViewSet(ModelViewSet):

    serializer_class = AnuncioSerializer

    def get_queryset(self):
        queryset = Anuncio.objects.select_related('id_campanha').filter(ativo='S',  id_campanha__data_inicial__lte=datetime.utcnow(),
                                                                        id_campanha__data_final__gte=datetime.utcnow(),
                                                                        id_campanha__ativa='S')

        '''#qs = Anuncio.objects.prefetch_related('id_campanha', 'id_placer').filter(ativo='S', id_campanha__data_inicial__lte=datetime.utcnow(), id_campanha__data_final__gte=datetime.utcnow(), id_campanha__ativa='S')

        #cod_campanhas = self.request.query_params.get('id', None)
        cod_place = self.request.query_params.get('cod', None)

        queryset = qs #Anuncio.objects.select_related('id_campanha').filter(ativo='S')

        if cod_place:
            #campanhas = cod_campanhas.split(',')
            #camp = list(map(int, campanhas))

         
            #queryset = Anuncio.objects.select_related('id_campanha').filter(id_campanha__in=camp, ativo='S', id_campanha__data_inicial__lte=datetime.utcnow(), id_campanha__data_final__gte=datetime.utcnow(), id_campanha__ativa='S')
            queryset = Anuncio.objects.prefetch_related('id_campanha').filter(id_place=cod_place, ativo='S',
                                        id_campanha__data_inicial__lte=datetime.utcnow(), id_campanha__data_final__gte=datetime.utcnow(), id_campanha__ativa='S')
        '''

        return queryset