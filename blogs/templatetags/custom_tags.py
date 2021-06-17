from django import template
register = template.Library()

from ..models import Blog

@register.simple_tag
def simple_count():
    return Blog.objects.count()