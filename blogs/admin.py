from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    """
    Django admin for the Blog model.
    """
    list_display = ('id', 'title', 'image', 'created', )
    readonly_fields=('show_url',)

    def show_url(self, instance):
        url = reverse('dashboard:blog_detail', kwargs={'pk': instance.pk})
        response = format_html("""<a href="{0}" target="_blank">{1}</a>""", url, url)
        return response

    show_url.short_description = 'Dashboard URL'

    # Displays HTML tags
    # Never set allow_tags to True against user submitted data!!!
    show_url.allow_tags = True


admin.site.register(Blog, BlogAdmin)
