from django.contrib import admin
from .models import Registros_Coautores, Coautores

class CouatorAdmin(admin.ModelAdmin):
    list_display = ('nome','documento', 'percentual_obra', 'arquivo')

admin.site.register(Coautores, CouatorAdmin)
