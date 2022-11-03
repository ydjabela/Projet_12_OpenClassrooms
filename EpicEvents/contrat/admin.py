
from django.contrib import admin
from .models import Contrat


class CustomContract(admin.ModelAdmin):
    fieldsets = [
        ('Client', {'fields': ['client']}),
        ('Sales contact', {'fields': ['sales_contact']}),
        ('Status', {'fields': ['status']}),
        ('Amount', {'fields': ['amount']}),
        ('Payment due', {'fields': ['payment_due']}),
    ]
    list_display = (
        'date_created',
        'client',
        'sales_contact',
        'status',
        'amount',
        'payment_due',
        'date_updated'
    )


admin.site.register(Contrat, CustomContract)
