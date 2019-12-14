from django.contrib import admin
from .models import Indicacoes, IndicacaoCliente

class IndicacaoClienteAdmin(admin.ModelAdmin):
    list_display = ('email_pai', 'email_filho', 'code_pai', 'code_filho', 'create_at')
    search_fields = ('email_pai', 'email_filho', 'code_pai', 'code_filho')
    list_filter = ('create_at',)



admin.site.register(Indicacoes)
admin.site.register(IndicacaoCliente, IndicacaoClienteAdmin)

