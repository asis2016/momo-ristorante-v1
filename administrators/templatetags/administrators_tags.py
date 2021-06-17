from django import template

register = template.Library()

from blogs.models import Blog
from bookings.models import Booking
from recipes.models import Recipe


@register.simple_tag
def model_entry_count():
    blog_count = Blog.objects.all().count()
    recipe_count = Recipe.objects.all().count()
    booking_count = Booking.objects.all().count()
    total = blog_count + recipe_count
    blog_count_percent = (blog_count / total) * 100
    recipe_count_percent = (recipe_count / total) * 100
    booking_count_percent = (booking_count / total) * 100

    data = [
        {
            'model': 'Blog',
            'total': round(blog_count_percent, 2)
        },
        {
            'model': 'Booking',
            'total': round(booking_count_percent, 2)
        },
        {
            'model': 'Recipe',
            'total': round(recipe_count_percent, 2)
        }
    ]
    return data
