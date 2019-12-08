from django.contrib import admin
from .models import Area_Atuacao

class Area_AtuacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)

# admin.site.register(Area_Atuacao,Area_AtuacaoAdmin)
