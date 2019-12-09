from django.contrib import admin
from .models import Clientes
from tools.render import Render
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'id', 'sexo', 'data_nascimento',
                    'cnpjcpf', 'celular', 'telefone')
    list_filter = ('tipo_pessoa', 'sexo','data_nascimento', 'data_cadastro',
         ('data_nascimento', DateRangeFilter), ('data_cadastro', DateRangeFilter),
    )
    search_fields = ('nome', 'id_usuario__username', 'cnpjcpf',)
    # filter_horizontal = ('atuacao',)
    autocomplete_fields = ('id_usuario', 'atuacao')
    actions = ['gera_pdf',]

    def gera_pdf(set, request, queryset):
        if queryset:
            return Render.render_to_pdf(request, queryset)

    gera_pdf.short_description = "Gerar PDF"
    # def gera_xls(set, request, queryset):
    #     if queryset:
    #         return Render.render_to_xls(request=request, queryset=queryset)

    # def teste(set, request, queryset):
    #     return Render.html_to_pdf_view(request, queryset)

    # set_default_password.short_description = "Definir senha padrão"
    # gera_xls.short_description = "Gerar Excel"


admin.site.register(Clientes, ClienteAdmin)


# Register your models here.
