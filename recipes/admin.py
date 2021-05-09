from django.contrib import admin

from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'create_by',)

admin.site.register(Recipe, RecipeAdmin)
