from django.urls import path, include
from servicos.api.views import ServicoExtentionsApi

urlpatterns = [
    path('servicos/<int:pk>', ServicoExtentionsApi.as_view())
]