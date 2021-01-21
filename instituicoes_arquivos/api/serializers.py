from rest_framework.serializers import ModelSerializer
from instituicoes_arquivos.models import Instituicoes_Arquivos
# from campanha.models import Anuncio
# from placer.models import Placer


# class PlaceSerializer(ModelSerializer):
#    class Meta:
#        model = Placer
#        fields = ['id', 'url_site']


class CampanhaSerializer(ModelSerializer):
    class Meta:
        model = Instituicoes_Arquivos
        fields = ['id', 'id_agencia', 'id_anunciante', 'nome', 'data_inicial', 'data_final']


# class AnuncioSerializer(ModelSerializer):
#    id_placer = PlaceSerializer(read_only=True, many=True)
#    class Meta:
#        model = Anuncio
#        fields = ['id', 'id_campanha', 'id_placer', 'tipo', 'nome', 'descricao','url_anunciante',
#                  'media', 'area2', 'area3', 'area4', 'qtd_visitas', 'qtd_cliques', 'ativo']
