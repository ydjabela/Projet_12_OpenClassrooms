from django.contrib import admin
from .models import Event


class CustomEvent(admin.ModelAdmin):
    fieldsets = [
        ('Client', {'fields': ['client']}),
        ('support_contact', {'fields': ['support_contact']}),
        ('event_status', {'fields': ['event_status']}),
        ('attendees', {'fields': ['attendees']}),
        ('event_date', {'fields': ['event_date']}),
        ('notes', {'fields': ['notes']}),
    ]
    list_display = (
        'date_created',
        'client',
        'support_contact',
        'attendees',
        'event_date',
        'notes'
    )


admin.site.register(Event, CustomEvent)
