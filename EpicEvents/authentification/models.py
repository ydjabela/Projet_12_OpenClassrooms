from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):

    first_name = models.CharField(max_length=25, null=False, blank=False)
    last_name = models.CharField(max_length=25, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    mobile = models.CharField(max_length=20, null=False, blank=False)
    company_name = models.CharField(max_length=250, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    def save(self, *args, **kwargs):
        super(Client, self).save(*args, **kwargs)
        return self
