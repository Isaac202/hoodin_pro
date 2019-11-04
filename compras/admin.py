from django.contrib import admin
from .models import Compras


class CompraCreditoAdmin(admin.ModelAdmin):
    list_display = ('id', 'codcliente', 'valor', 'data', 'msg_cielo', 'codigo_compra_cielo')
    list_filter = ('forma_pagamento',)

admin.site.register(Compras, CompraCreditoAdmin)