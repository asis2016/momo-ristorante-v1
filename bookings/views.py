"""
    bookings/views.py
    -----------------
"""
from django.views.generic import ListView, DetailView, DeleteView

from .models import Booking


class BookingListView(ListView):
    """ Booking List view. """
    model = Booking
    template_name = 'bookings/bookings.html'
    context_object_name = 'bookings'


class BookingDetailView(DetailView):
    """
    Booking detail view.
    """
    model = Booking
    template_name = 'bookings/detail.html'
    context_object_name = 'booking'


# Dashboard
class DashboardBookingListView(ListView):
    """
    The Booking ListView for the Dashboard.
    """
    model = Booking
    template_name = 'bookings/dashboard/list.html'
    context_object_name = 'bookings'


class DashboardBookingDetailView(DetailView):
    """
    The Booking DetailView for the Dashboard.
    """
    model = Booking
    template_name = 'bookings/dashboard/detail.html'
    context_object_name = 'booking'


class DashboardBookingDeleteView(DeleteView):
    """
    The Booking DeleteView for the Dashboard.
    """
    model = Booking
    template_name = 'bookings/dashboard/delete.html'
    context_object_name = 'booking'
