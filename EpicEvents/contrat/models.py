from django.db import models
from django.contrib.auth.models import User
from authentification.models import Client


class Contrat(models.Model):
    sales_contact = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    date_updated = models.DateTimeField(auto_now=True,  null=False, blank=False)
    status = models.BooleanField(null=False, blank=False)
    amount = models.FloatField(null=False, blank=False)
    payment_due = models.DateTimeField(null=False, blank=False)

    def save(self, *args, **kwargs):
        super(Contract, self).save(*args, **kwargs)
        return self
