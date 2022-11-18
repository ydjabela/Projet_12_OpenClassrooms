from django.contrib import admin
# Locals:
from .models import Client, User


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


class CustomUser(admin.ModelAdmin):
    list_display = (
        'date_joined',
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'role'
    )


admin.site.register(Client, CustomClient)
admin.site.register(User, CustomUser)
