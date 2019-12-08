from django.contrib import admin
from .models import Clientes


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome','id', 'sexo', 'data_nascimento', 'cnpjcpf', 'celular', 'telefone')
    list_filter = ('tipo_pessoa', 'sexo',)
    search_fields = ('nome', 'id_usuario__username', 'cnpjcpf',)
    # filter_horizontal = ('atuacao',)
    autocomplete_fields = ('id_usuario', 'atuacao')



admin.site.register(Clientes, ClienteAdmin)


# Register your models here.
