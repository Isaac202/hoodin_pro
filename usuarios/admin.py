from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from usuarios.models import UserConfirm, Confuguracao

User = get_user_model()

class UserConfirmAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'confirmed')
    search_fields = ('user__username',)
    list_filter = ('confirmed', 'created_at',)

admin.site.register(UserConfirm, UserConfirmAdmin)
admin.site.register(User, BaseUserAdmin)
admin.site.register(Confuguracao)