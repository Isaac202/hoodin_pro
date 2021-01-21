from django.contrib import admin
from .models import Instituicoes_Arquivos, Avaliadores




class Instituicoes_ArquivosAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_instituicao', 'id_avaliador', 'nome', 'valor',
                    'data_inicial', 'data_final', 'ativa')
    list_filter = ('id_instituicao', 'id_avaliador', 'ativa')



# class AnuncioAdmin(admin.ModelAdmin):
#    list_display = ('id', 'id_campanha', 'nome', 'ativo')
#    list_filter = ('id_campanha','ativo')



admin.site.register(Instituicoes_Arquivos, Instituicoes_ArquivosAdmin)
# admin.site.register(Anuncio, AnuncioAdmin)

# Register your models here.
