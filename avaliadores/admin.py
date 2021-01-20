from django.contrib import admin
from .models import Avaliadores

class AvaliadoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)

admin.site.register(Avaliadores, AvaliadoresAdmin)


# Register your models here.
