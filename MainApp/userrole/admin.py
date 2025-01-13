from django.contrib import admin

from .Models.user import User
from .Models.role import Role

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_active', 'is_admin', 'created_at')
    search_fields = ('username', 'email')
    list_filter = ('is_admin', 'role')

admin.site.register(Role)
admin.site.register(User, UserAdmin)
