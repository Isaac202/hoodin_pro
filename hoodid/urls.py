from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from home.views import sair
from django.contrib.auth import views as auth_views
from extensoes.views import ExtensoesCreate
from extensoes.views import ExtensoesList
from extensoes.views import ExtensoesUpdate
from extensoes.views import ExtensoesDelete

from clientes.views import ClientesCreate
from clientes.views import ClientesList
from clientes.views import ClientesUpdate
from clientes.views import ClientesDelete

from clientes.views import ConfirmacaoCadadtro


from servicos.views import ServicosCreate
from servicos.views import ServicosList
from servicos.views import ServicosUpdate
from servicos.views import ServicosDelete
from servicos.api.viewsets import ServicoViewSet

from indicacoes.views import IndicacoesCreate
from indicacoes.views import IndicacoesList
from indicacoes.views import IndicacoesUpdate
from indicacoes.views import IndicacoesDelete

from precos.views import PrecosCreate
from precos.views import PrecosList
from precos.views import PrecosUpdate
from precos.views import PrecosDelete

from area_atuacao.views import Area_AtuacaoCreate
from area_atuacao.views import Area_AtuacaoList
from area_atuacao.views import Area_AtuacaoUpdate
from area_atuacao.views import Area_AtuacaoDelete
from rest_framework import routers
# from servicos.views import ServicosExtensoesCreate

#from servicos.views import ServicosExtensoesList
#from servicos.views import ServicosExtensoesUpdate

from registros.views import RegistrosCreate, BasicUploadView
from clientes.api.viewsets import ClienteViewSet
from area_atuacao.views import Area_AtuacaoListCriacaoPublicitaria
router = routers.SimpleRouter()
router.register(r'api/clientes', ClienteViewSet)
router.register(r'api/servicos', ServicoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', sair, name='logout'),

    path('lista_extensoes/', ExtensoesList.as_view(), name='lista_extensoes'),
    path('novo_extensoes/', ExtensoesCreate.as_view(), name='novo_extensoes'),
    path('atualiza_extensoes/<int:pk>/', ExtensoesUpdate.as_view(), name='atualiza_extensoes'),
    path('delete_extensoes/<int:pk>/', ExtensoesDelete.as_view(), name='delete_extensoes'),
    
    path('clientes/', include('clientes.urls')),

    path('lista_servicos/', ServicosList.as_view(), name='lista_servicos'),
    path('novo_servicos/', ServicosCreate.as_view(), name='novo_servicos'),
    path('atualiza_servicos/<int:pk>/', ServicosUpdate.as_view(), name='atualiza_servicos'),
    path('delete_servicos/<int:pk>/', ServicosDelete.as_view(), name='delete_servicos'),

    path('lista_indicacoes/', IndicacoesList.as_view(), name='lista_indicacoes'),
    path('novo_indicacoes/', IndicacoesCreate.as_view(), name='novo_indicacoes'),
    path('atualiza_indicacoes/<int:pk>/', IndicacoesUpdate.as_view(), name='atualiza_indicacoes'),
    path('delete_indicacoes/<int:pk>/', IndicacoesDelete.as_view(), name='delete_indicacoes'),

    path('accounts/', include('usuarios.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('lista_precos/', PrecosList.as_view(), name='lista_precos'),
    path('novo_precos/', PrecosCreate.as_view(), name='novo_precos'),
    path('atualiza_precos/<int:pk>/', PrecosUpdate.as_view(), name='atualiza_precos'),
    path('delete_precos/<int:pk>/', PrecosDelete.as_view(), name='delete_precos'),
    path('api/confirmar/', ConfirmacaoCadadtro.as_view()),


    path('lista_area_atuacao_criacaopublicitaria/', Area_AtuacaoList.as_view(), name='lista_area_atuacao_criacaopublicitaria'),
    path('lista_area_atuacao_desenhogravura/', Area_AtuacaoList.as_view(), name='lista_area_atuacao_desenhogravura'),
    path('lista_area_atuacao_escultura/', Area_AtuacaoList.as_view(), name='lista_area_atuacao_escultura'),
    path('lista_area_atuacao_filmedocumentario/', Area_AtuacaoList.as_view(), name='lista_area_atuacao_filmedocumentario'),
    path('lista_area_atuacao_fotografia/', Area_AtuacaoList.as_view(), name='lista_area_atuacao_fotografia'),
    path('lista_area_atuacao_musica/', Area_AtuacaoList.as_view(), name='lista_area_atuacao_musica'),
    path('lista_area_atuacao_palestraconferencia/', Area_AtuacaoList.as_view(), name='lista_area_atuacao_palestraconferencia'),
    path('lista_area_atuacao_pintura/', Area_AtuacaoList.as_view(), name='lista_area_atuacao_pintura'),
    path('lista_area_atuacao_poesia/', Area_AtuacaoList.as_view(), name='lista_area_atuacao_poesia'),
    path('lista_area_atuacao_projetoarquitetonico/', Area_AtuacaoList.as_view(), name='lista_area_atuacao_projetoarquitetonico'),
    path('lista_area_atuacao_projetodiverso/', Area_AtuacaoList.as_view(), name='lista_area_atuacao_projetodiverso'),
    path('lista_area_atuacao_software/', Area_AtuacaoList.as_view(), name='lista_area_atuacao_software'),
    path('lista_area_atuacao_teatrocoreografia/', Area_AtuacaoList.as_view(), name='lista_area_atuacao_teatrocoreografia'),
    path('lista_area_atuacao_texto/', Area_AtuacaoList.as_view(), name='lista_area_atuacao_texto'),
    path('novo_area_atuacao/', Area_AtuacaoCreate.as_view(), name='novo_area_atuacao'),
    path('atualiza_area_atuacao/<int:pk>/', Area_AtuacaoUpdate.as_view(), name='atualiza_area_atuacao'),
    path('delete_area_atuacao/<int:pk>/', Area_AtuacaoDelete.as_view(), name='delete_area_atuacao'),

    path('registrar/', RegistrosCreate.as_view(), name='registrar'),
    path('upload/', BasicUploadView.as_view(), name='upload'),

    # path('novo_servicosextensoes/', ServicosExtensoesCreate.as_view(), name='novo_servicosextensoes'),

]

admin.site.site_header = "Hoodid"

admin.site.index_title = "Hoodid"

admin.site.site_title = "Painel"