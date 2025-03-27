from django.contrib import admin

# Register your models here.
from .models import Registration


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'event', 'email', 'created_at', 'created_at')
    list_filter = ('event', 'created_at')
    search_fields = ('name', 'email')