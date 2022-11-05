from django.db import models
from authentification.models import Client, User
from contrat.models import Contrat


class EventStatus(models.Model):
    CREATED = 'created'
    INPROGRESS = 'in_progress'
    FINISHED = 'finished'
    EVENT_STATUS = (
        (CREATED, 'created'),
        (INPROGRESS, 'in_progress'),
        (FINISHED, 'finished')
    )

    event_status = models.CharField(max_length=20, choices=EVENT_STATUS)

    def save(self, *args, **kwargs):
        super(EventStatus, self).save(*args, **kwargs)
        return self


class Event(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    date_updated = models.DateTimeField(auto_now=True, null=False, blank=False)
    support_contact = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)
    event_status = models.ForeignKey(to=EventStatus, on_delete=models.CASCADE)
    contrat = models.ForeignKey(Contrat, on_delete=models.SET_NULL, null=True, blank=False)
    attendees = models.IntegerField(null=False, blank=False)
    event_date = models.DateTimeField(null=False, blank=False)
    notes = models.TextField(null=False, blank=False)

    def save(self, *args, **kwargs):
        super(Event, self).save(*args, **kwargs)
        return self
