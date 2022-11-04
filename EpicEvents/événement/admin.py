from django.contrib import admin
from .models import Event, EventStatus


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


class CustomStatusEvent(admin.ModelAdmin):
    fieldsets = [
        ('event_status', {'fields': ['event_status']}),
    ]
    list_display = (
        'event_status',
    )


admin.site.register(Event, CustomEvent)
admin.site.register(EventStatus, CustomStatusEvent)
