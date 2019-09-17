from django.contrib import admin
from .models import Extensoes

class ExtensoesAdmin(admin.ModelAdmin):
    list_display = ('codextensao', 'nome')
    search_fields = ('nome',)

admin.site.register(Extensoes,ExtensoesAdmin)
