from django.contrib import admin

# Register your models here.
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'capacity', 'created_at')
    list_filter = ('date', 'location')
    search_fields = ('title', 'location')