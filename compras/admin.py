from django.contrib import admin
from .models import Compras
from tools.render import RenderPDF as Render
# from django.contrib.admin import DateFieldListFilter
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
# from daterangefilter.filters import PastDateRangeFilter, FutureDateRangeFilter

class CompraCreditoAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'valor', 'data',
                    'msg_cielo', 'codigo_compra_cielo')
    list_filter = ('forma_pagamento', 'autorizado', 'data'    ,
        ('data', DateRangeFilter),
    )
    search_fields = ('id_cliente__nome', 'msg_cielo', 'codigo_compra_cielo')
    actions = ['gera_pdf', ]

    def gera_pdf(set, request, queryset):
        if queryset:
            return Render.render_to_pdf(request, queryset, 
            description="Relatório de compras",
            template='tools/pdf_compras.html')

    gera_pdf.short_description = "Gerar PDF"


admin.site.register(Compras, CompraCreditoAdmin)
