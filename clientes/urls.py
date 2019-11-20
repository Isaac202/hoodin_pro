from django.urls import path
from clientes.views import ClientesCreate
from clientes.views import ClientesList
from clientes.views import ClientesUpdate
from clientes.views import ClientesDelete

from clientes.views import ConfirmacaoCadadtro


app_name = "cliente"

urlpatterns = [
    path('list/', ClientesList.as_view(), name='list'),
    path('new/', ClientesCreate.as_view(), name='new'),
    path('update/', ClientesUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', ClientesDelete.as_view(), name='delete'),
    path('api/confirmar/', ConfirmacaoCadadtro.as_view()),
]