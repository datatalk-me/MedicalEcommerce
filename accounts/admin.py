from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display: list = ('email', 'username', 'first_name', 'last_name','last_login','is_staff', 'is_admin', 'is_superuser')
    search_fields: list = ('email', 'username', 'first_name', 'last_name')
    list_display_links: list = ('email', 'username', 'first_name', 'last_name')
    readonly_fields: list = ('date_joined', 'last_login')
    ordering: list = ('-date_joined',)

    filter_horizontal: list = ()
    list_filter: list = ()
    fieldsets: list = ()


admin.site.register(Account, AccountAdmin)
