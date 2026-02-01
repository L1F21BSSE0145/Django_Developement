from django.contrib import admin
from .models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display=('username','email','password','created_at')
    search_fields = ('username', 'email')
    list_filter = ('created_at',)

