from django.contrib import admin

from .models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    """
    Django admin for the Recipe model.
    """
    list_display = ('id', 'title', 'image_url', 'author', 'created',)


admin.site.register(Recipe, RecipeAdmin)
