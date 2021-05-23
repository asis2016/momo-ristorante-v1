from django.contrib import admin

from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'created', 'modified')


admin.site.register(Blog, BlogAdmin)
