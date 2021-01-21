from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from home.views import sair, CotratoView
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


from servicos.views import ServicosCreate, TabelaPrecos
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

from registros.views import RegistrosCreate, BasicUploadView, MeusRegistrosList, TesteCreateView,  certificadoPDFView, DownloadCertificadoList
from clientes.api.viewsets import ClienteViewSet

from codigos_promocionais.views import Codigos_PromocionaisCreate
from codigos_promocionais.views import Codigos_PromocionaisList
from codigos_promocionais.views import Codigos_PromocionaisUpdate
from codigos_promocionais.views import Codigos_PromocionaisDelete

from instituicoes.views import InstituicoesCreate
from instituicoes.views import InstituicoesList
from instituicoes.views import InstituicoesUpdate
from instituicoes.views import InstituicoesDelete

from avaliadores.views import AvaliadoresCreate
from avaliadores.views import AvaliadoresList
from avaliadores.views import AvaliadoresUpdate
from avaliadores.views import AvaliadoresDelete

from instituicoes_arquivos.views import Instituicoes_ArquivosCreate
from instituicoes_arquivos.views import Instituicoes_ArquivosList
from instituicoes_arquivos.views import Instituicoes_ArquivosUpdate
from instituicoes_arquivos.views import Instituicoes_ArquivosDelete


from area_atuacao.views import Area_AtuacaoListCriacaoPublicitaria
router = routers.SimpleRouter()
router.register(r'api/clientes', ClienteViewSet)
router.register(r'api/servicos', ServicoViewSet)

from compras.views import CompraCreditoCreate

# from django_pdfkit import PDFView



urlpatterns = [
    path('api/', include("api.urls")),
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
    path('meus-registros/', MeusRegistrosList.as_view(), name='meus_registros'),
    path('upload/', BasicUploadView.as_view(), name='upload'),
    path('teste/', TesteCreateView.as_view(), name='teste'),
    # path('topdf/<int:id_registro>', to_pdfkit, name='pdf'),
    path('topdf/<int:id_registro>', certificadoPDFView , name='pdf'),

    path('lista_codigos_promocionais/', Codigos_PromocionaisList.as_view(), name='lista_codigos_promocionais'),
    path('novo_codigos_promocionais/', Codigos_PromocionaisCreate.as_view(), name='novo_codigos_promocionais'),
    path('atualiza_codigos_promocionais/<int:pk>/', Codigos_PromocionaisUpdate.as_view(), name='atualiza_codigos_promocionais'),
    path('delete_codigos_promocionais/<int:pk>/', Codigos_PromocionaisDelete.as_view(), name='delete_codigos_promocionais'),
    path('compra/', CompraCreditoCreate.as_view(), name='credito'),
    path('tabela-de-precos/', TabelaPrecos.as_view(), name='tabela_de_precos'),
    path('contrato/', CotratoView.as_view(), name='contrato'),

    path('download_certificado/', DownloadCertificadoList.as_view(), name='download_certificado'),
    # path('novo_servicosextensoes/', ServicosExtensoesCreate.as_view(), name='novo_servicosextensoes'),

    path('lista_instituicoes/', InstituicoesList.as_view(), name='lista_instituicoes'),
    path('novo_instituicoes/', InstituicoesCreate.as_view(), name='novo_instituicoes'),
    path('atualiza_instituicoes/<int:pk>/', InstituicoesUpdate.as_view(), name='atualiza_instituicoes'),
    path('delete_instituicoes/<int:pk>/', InstituicoesDelete.as_view(), name='delete_instituicoes'),
    path('atualiza_instituicoes/<int:pk>/', InstituicoesUpdate.as_view(), name='atualiza_instituicoes'),

    path('lista_avaliadores/', AvaliadoresList.as_view(), name='lista_avaliadores'),
    path('avaliadores/', AvaliadoresCreate.as_view(), name='novo_avaliadores'),
    path('atualiza_avaliadores/<int:pk>/', AvaliadoresUpdate.as_view(), name='atualiza_avaliadores'),
    path('delete_avaliadores/<int:pk>/', AvaliadoresDelete.as_view(), name='delete_avaliadores'),

    path('lista_instituicoes_arquivos/', Instituicoes_ArquivosList.as_view(), name='lista_instituicoes_arquivos'),
    path('instituicoes_arquivos/', Instituicoes_ArquivosCreate.as_view(), name='novo_instituicoes_arquivos'),
    path('atualiza_instituicoes_arquivos/<int:pk>/', Instituicoes_ArquivosUpdate.as_view(), name='atualiza_instituicoes_arquivos'),
    path('delete_instituicoes_arquivos/<int:pk>/', Instituicoes_ArquivosDelete.as_view(), name='delete_instituicoes_arquivos'),
]

admin.site.site_header = "Hoodid"

admin.site.index_title = "Hoodid"

admin.site.site_title = "Painel"
