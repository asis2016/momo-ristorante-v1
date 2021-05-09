"""
    bookings/models.py
    ------------------
    In booking, any guest can reserve a table.
    He / She can post a note also.
    Optional: New booking is notified to the manager via email.
    Only employees (all as of v.1.0) can view booking information.
"""
import uuid
from django.contrib.auth import get_user_model
from django.db import models


class Booking(models.Model):
    """ Booking model as of v.1.0 """
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
    status = models.BooleanField(default=0)
    create_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.fullname)
