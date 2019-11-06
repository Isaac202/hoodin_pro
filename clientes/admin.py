from django.contrib import admin
from .models import Clientes


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sexo', 'data_nascimento', 'cnpjcpf', 'celular', 'telefone')
    list_filter = ('tipo_pessoa',)
    search_fields = ('nome', 'email')



admin.site.register(Clientes, ClienteAdmin)


# Register your models here.
