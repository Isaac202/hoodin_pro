from django.contrib import admin
from .models import Servicos

class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome','preco','tamanho', 'servico_digitalizacao')
    search_fields = ('nome',)
    list_filter = ('servico_digitalizacao','extensoes')
    # filter_vertical = ('extensoes',)
    autocomplete_fields = ('extensoes', )  


admin.site.register(Servicos, ServicoAdmin)
