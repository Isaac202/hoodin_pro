from django.contrib import admin
from .models import Clientes
from tools.render import RenderPDF as Render
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'id', 'sexo', 'data_nascimento',
                    'cnpjcpf', 'celular', 'telefone')
    list_filter = ('tipo_pessoa', 'sexo', 'data_nascimento', 'data_cadastro',
                   ('data_nascimento',
                    DateRangeFilter), ('data_cadastro', DateRangeFilter),
                   )
    search_fields = ('nome', 'id_usuario__username', 'cnpjcpf',)
    # filter_horizontal = ('atuacao',)
    autocomplete_fields = ('id_usuario', 'atuacao')
    actions = ['gera_pdf_anailitico', 'gera_pdf_sintetico']

    def gera_pdf_anailitico(set, request, queryset):
        if queryset:
            return Render.render_to_pdf(
                request,
                queryset,
                description="Relatório de clientes Analítico"
            )

    def gera_pdf_sintetico(set, request, queryset):
        if queryset:
            return Render.render_to_pdf(
                request,
                queryset,
                template="tools/pdf_clientes_sintetico.html",
                description="Relatório de clientes Sintético"
            )

    gera_pdf_anailitico.short_description = "Relatório Analítico"
    gera_pdf_sintetico.short_description = "Relatório Sintético"

    # def gera_xls(set, request, queryset):
    #     if queryset:
    #         return Render.render_to_xls(request=request, queryset=queryset)

    # def teste(set, request, queryset):
    #     return Render.html_to_pdf_view(request, queryset)

    # set_default_password.short_description = "Definir senha padrão"
    # gera_xls.short_description = "Gerar Excel"


admin.site.register(Clientes, ClienteAdmin)


# Register your models here.
