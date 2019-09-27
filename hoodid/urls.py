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

from servicos.views import ServicosCreate
from servicos.views import ServicosList
from servicos.views import ServicosUpdate
from servicos.views import ServicosDelete

from indicacoes.views import IndicacoesCreate
from indicacoes.views import IndicacoesList
from indicacoes.views import IndicacoesUpdate
from indicacoes.views import IndicacoesDelete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', sair, name='logout'),

    path('lista_extensoes/', ExtensoesList.as_view(), name='lista_extensoes'),
    path('novo_extensoes/', ExtensoesCreate.as_view(), name='novo_extensoes'),
    path('atualiza_extensoes/<int:pk>/', ExtensoesUpdate.as_view(), name='atualiza_extensoes'),
    path('delete_extensoes/<int:pk>/', ExtensoesDelete.as_view(), name='delete_extensoes'),

    path('lista_clientes/', ClientesList.as_view(), name='lista_clientes'),
    path('novo_clientes/', ClientesCreate.as_view(), name='novo_clientes'),
    path('atualiza_clientes/<int:pk>/', ClientesUpdate.as_view(), name='atualiza_clientes'),
    path('delete_clientes/<int:pk>/', ClientesDelete.as_view(), name='delete_clientes'),

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

]

admin.site.site_header = "Hoodid"

admin.site.index_title = "Hoodid"

admin.site.site_title = "Painel"