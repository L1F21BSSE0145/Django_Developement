from django.contrib import admin
from .models import Register

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "password", "created_at")
    search_fields = ("username", "email")
