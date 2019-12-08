from django.contrib import admin
from .models import Clientes
from tools.render import Render


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'id', 'sexo', 'data_nascimento',
                    'cnpjcpf', 'celular', 'telefone')
    list_filter = ('tipo_pessoa', 'sexo',)
    search_fields = ('nome', 'id_usuario__username', 'cnpjcpf',)
    # filter_horizontal = ('atuacao',)
    autocomplete_fields = ('id_usuario', 'atuacao')
    actions = ['gera_pdf', 'gera_xls',]

    def gera_pdf(set, request, queryset):
        if queryset:
            return Render.render_to_pdf(request=request, clientes=queryset)
        else:
            queryset = Clientes.objects.all().order_by('nome')
            return Render.render_to_pdf(request=request, clientes=queryset)

    def gera_xls(set, request, queryset):
        if queryset:
            return Render.render_to_xls(request=request, queryset=queryset)

    # def teste(set, request, queryset):
    #     return Render.some_view(request)

    # set_default_password.short_description = "Definir senha padrão"
    gera_pdf.short_description = "Gerar PDF"
    gera_xls.short_description = "Gerar Excel"


admin.site.register(Clientes, ClienteAdmin)


# Register your models here.
