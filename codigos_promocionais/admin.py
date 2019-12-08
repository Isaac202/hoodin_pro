from django.contrib import admin
from .models import Codigos_Promocionais, GeneratePromocionalCode


class GerarCodigoAdmin(admin.ModelAdmin):
    list_display = ("valor", 'quantidade', 'data_inicio', 'data_fim','generated')
    list_filter = ('generated',)
    search_fields = ('email', 'cnpjcpf', 'nome')


class CodigoPromocionalAdmin(admin.ModelAdmin):
    list_display = ('promotor', 'qrcode', 'data_emissao')
    list_filter = ('resgate',)
    search_fields = ('qrcode', 'email', 'cnpjcpf', 'nome')

admin.site.register(Codigos_Promocionais, CodigoPromocionalAdmin)
admin.site.register(GeneratePromocionalCode, GerarCodigoAdmin)
