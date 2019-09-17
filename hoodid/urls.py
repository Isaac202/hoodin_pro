from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from home.views import sair
from django.contrib.auth import views as auth_views

from extensoes.views import ExtensoesCreate
from extensoes.views import ExtensoesList
from extensoes.views import ExtensoesUpdate
from extensoes.views import ExtensoesDelete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', sair, name='logout'),
    path('extensoes/', ExtensoesCreate.as_view(), name='novo_extensoes'),
    path('lista_extensoes/', ExtensoesList.as_view(), name='lista_extensoes'),
    path('atualiza_extensoes/<int:pk>/', ExtensoesUpdate.as_view(), name='atualiza_extensoes'),
    path('delete_extensoes/<int:pk>/', ExtensoesDelete.as_view(), name='delete_extensoes'),

]

admin.site.site_header = "Hoodid"

admin.site.index_title = "Hoodid"

admin.site.site_title = "Painel"