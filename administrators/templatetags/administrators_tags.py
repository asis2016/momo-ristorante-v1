from django import template
from helper.quick_stat_template import quick_stat_helper_template
from helper.icon import Icon

register = template.Library()

from blogs.models import Blog
from bookings.models import Booking
from recipes.models import Recipe


@register.simple_tag
def model_entry_count():
    blog_count = Blog.objects.all().count()
    recipe_count = Recipe.objects.all().count()
    booking_count = Booking.objects.all().count()
    total = blog_count + recipe_count + booking_count
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


@register.simple_tag
def blog_quick_stat():
    """
    Renders quick stat for Blog in Dashboard.
    """
    total = Blog.objects.count()
    html = quick_stat_helper_template('Blog', total, Icon.BLOG.value)
    return html


@register.simple_tag
def booking_quick_stat():
    """
    Renders quick stat for Booking in Dashboard.
    """
    total = Booking.objects.count()
    html = quick_stat_helper_template('Booking', total, Icon.CALENDAR.value)
    return html


@register.simple_tag
def comment_quick_stat():
    """
    Renders quick stat for comment in Dashboard.
    """
    html = quick_stat_helper_template('Comments', 20, Icon.COMMENT.value)
    return html


@register.simple_tag
def recipe_quick_stat():
    """
    Renders quick stat for Recipe in Dashboard.
    """
    total = Recipe.objects.count()
    html = quick_stat_helper_template('Recipe', total, Icon.RECIPE.value)
    return html