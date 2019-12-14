from django.contrib import admin
from registros.models import Registros, ArquivoRegistro
from rangefilter.filter import DateRangeFilter
from tools.render import Render

class ArquivoAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'name', 'version', 'value', 'resume')
    list_filter = ('paid', 'create_at')
    search_fields = ('shar256','id_usuario__username', 'name', "resume")


class RegistroAdmin(admin.ModelAdmin):
    list_display = ('id_usuario','id_cliente', 'codservico', 'descricao', 'data')
    list_filter = ('data', 'codservico',
                   ('data', DateRangeFilter),
                   )
    search_fields = ('codservico', 'id_usuario__username',
                     "id_cliente__cnpjcpf")
    autocomplete_fields = ('id_usuario', "id_cliente", 'codservico',)
    actions = ['gera_pdf','gera_pdf_total' ]
    show_full_result_count = True
    

    def gera_pdf(set, request, queryset):
        if queryset:
            return Render.render_to_pdf(request, queryset,
                                        description="Relatório de Registros",
                                        template="tools/pdf_registros.html"
                                        )

    def gera_pdf_total(set, request, queryset):
        queryset = queryset.objects.all().aggregate(total=Sum('valor'), count=Count('codservico'))
        # queryset = queryset..values('id_usuario', 'codservico')
        return Render.render_to_pdf(request, queryset,
                                        description="Ryelatório de Registros",
                                        template="tools/pdf_registros_total.html"
                                        )

    gera_pdf.short_description = "Registros realizados"
    gera_pdf_total.short_description = "Registros realizados totalizados"


admin.site.register(Registros, RegistroAdmin)
admin.site.register(ArquivoRegistro, ArquivoAdmin)

