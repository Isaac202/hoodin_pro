from django.contrib import admin
from .models import Instituicoes
from tools.render import RenderPDF as Render

class InstituicoesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'create_at')
    search_fields = ('nome', 'code_filho')
    list_filter = ('create_at',)
    actions = ['gera_pdf',]

    def gera_pdf(set, request, queryset):
        if queryset:
            return Render.render_to_pdf(request, queryset,
                                        description="Relatório de Instituiçoes",
                                        template="tools/pfd_instituicoes.html"
                                        )
    gera_pdf.short_description = "Gerar pdf"


admin.site.register(Instituicoes, InstituicoesAdmin)
