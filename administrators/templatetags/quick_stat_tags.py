from django import template

register = template.Library()

from helper.quick_stat_template import template

from blogs.models import Blog


@register.simple_tag
def quick_stat():
    _total = Blog.objects.count()
    html = template('Blog', _total, 'fa-th-large')
    return html
