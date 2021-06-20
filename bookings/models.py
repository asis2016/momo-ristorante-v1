"""
    bookings/models.py
    ------------------
    In booking, any guest can reserve a table.
    He / She can post a note also.
    Optional: New booking is notified to the manager via email.
    Only employees (all as of v.1.0) can view booking information.
"""
import uuid

from django.db import models

from core.models import TimeStampedModel


class Booking(TimeStampedModel):
    """
    Booking model as of v.1.0
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.TextField()
    person = models.IntegerField()
    note = models.TextField(blank=True)
    is_approved = models.BooleanField(default=1)

    def __str__(self):
        return str(self.fullname)
