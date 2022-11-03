from django.contrib import admin
# Locals:
from .models import Client


# Register client
class CustomClient(admin.ModelAdmin):
    """
    Allow Admins to Create/Update/Delete Clients
    """
    fieldsets = [
        ('First name', {'fields': ['first_name']}),
        ('Last name', {'fields': ['last_name']}),
        ('Email', {'fields': ['email']}),
        ('Phone', {'fields': ['phone']}),
        ('Mobile', {'fields': ['mobile']}),
        ('Company name', {'fields': ['company_name']}),
        ('Sales contact', {'fields': ['sales_contact']}),
    ]
    list_display = (
        'date_created',
        'first_name',
        'last_name',
        'email',
        'phone',
        'mobile',
        'company_name',
        'sales_contact',
        'date_updated'
    )


admin.site.register(Client, CustomClient)
