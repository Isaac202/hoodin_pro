from django.contrib import admin
from .models import Codigos_Promocionais, GeneratePromocionalCode
from tools.render import RenderPDF
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from codigos_promocionais.actions import write_code

class GerarCodigoAdmin(admin.ModelAdmin):
    list_display = ("valor", 'quantidade', 'data_inicio',
                    'data_fim', 'generated')
    list_filter = ('generated',)
    search_fields = ('email', 'cnpjcpf', 'nome')


class CodigoPromocionalAdmin(admin.ModelAdmin):
    list_display = ('qrcode','valor', 'data_emissao', 'data_limite',
                    'data_resgate', "promotor")
    list_filter = ('resgate', 'data_emissao', 'data_limite', 'data_resgate',
                   ('data_emissao',
                    DateRangeFilter),
                    ('data_resgate', DateRangeFilter),
                    ('data_limite', DateRangeFilter),
                   )
    search_fields = ('qrcode', 'email', 'cnpjcpf', 'nome')
    actions = ['gera_pdf','gera_cartao']

    def gera_pdf(set, request, queryset):
        if queryset:
            return RenderPDF.render_to_pdf(
                request,
                queryset,
                template="tools/pdf_cod_promocional.html",
                description="Relatório Códigos promocionais gerados"
            )


    def gera_cartao(set, request, queryset):
        return write_code(queryset)

    gera_cartao.short_description = "Gerar Cartao"
    gera_pdf.short_description = "Gerar PDF"


admin.site.register(Codigos_Promocionais, CodigoPromocionalAdmin)
admin.site.register(GeneratePromocionalCode, GerarCodigoAdmin)


