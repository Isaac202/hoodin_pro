from django.contrib import admin
from .models import Registros, ArquivoRegistro
from rangefilter.filter import DateRangeFilter
from tools.render import Render

class RegistroAdmin(admin.ModelAdmin):
    list_display = ('id_usuario','codservico','data')
    list_filter = ('data', 'codservico',
        ('data', DateRangeFilter),
    )
    search_fields = ('codservico', 'id_usuario__username', "id_cliente__cnpjcpf")
    autocomplete_fields = ('id_usuario', "id_cliente", 'codservico',)
    actions = ['gera_pdf',]

    def gera_pdf(set, request, queryset):
        if queryset:
            return Render.render_to_pdf(request, queryset,
                description="Relatório de Registros",
                template="tools/pdf_registros.html"
            )

    gera_pdf.short_description = "Gerar PDF"

admin.site.register(Registros, RegistroAdmin)
admin.site.register(ArquivoRegistro)
