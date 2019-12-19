from django.contrib import admin
from .models import Indicacoes, IndicacaoCliente
from tools.render import Render

class IndicacaoClienteAdmin(admin.ModelAdmin):
    list_display = ('email_pai', 'email_filho', 'code_pai', 'code_filho', 'create_at')
    search_fields = ('email_pai', 'email_filho', 'code_pai', 'code_filho')
    list_filter = ('create_at',)
    actions = ['gera_pdf',]

    def gera_pdf(set, request, queryset):
        if queryset:
            return Render.render_to_pdf(request, queryset,
                                        description="Relatório de Indicações clientes",
                                        template="tools/pfd_indicacao_cliente.html"
                                        )
    gera_pdf.short_description = "Gerar pdf"
admin.site.register(Indicacoes)
admin.site.register(IndicacaoCliente, IndicacaoClienteAdmin)

 