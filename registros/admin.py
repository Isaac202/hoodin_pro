from django.contrib import admin
from .models import Registros, ArquivoRegistro


class RegistroAdmin(admin.ModelAdmin):
    list_display = ('id_usuario','data')
    list_filter = ('data', 'codservico',)
    search_fields = ('codservico', 'id_usuario__username', "id_cliente__cnpjcpf")
    autocomplete_fields = ('id_usuario', "id_cliente", 'codservico',)

admin.site.register(Registros, RegistroAdmin)
admin.site.register(ArquivoRegistro)
