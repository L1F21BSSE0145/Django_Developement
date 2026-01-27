from django.contrib import admin
from .models import Account

class AccountAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email','created_at')
    search_fields = ('full_name', 'email')

admin.site.register(Account, AccountAdmin)

