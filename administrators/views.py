from django.db import connection
from django.views import generic

from blogs.models import Blog
from bookings.models import Booking
from recipes.models import Recipe


class AdministratorDashboard(generic.TemplateView):
    """
    The templateview for Administrator
    """
    template_name = 'administrators/Dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super(AdministratorDashboard, self).get_context_data(**kwargs)
        context['latest_five_blog'] = Blog.objects.all()[:5]
        context['latest_five_recipes'] = Recipe.objects.all()[:5]
        context['pending_bookings'] = Booking.objects.all()[:5]
        return context
