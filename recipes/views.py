"""
    recipes/views.py
    ----------------
"""
from django.views.generic import ListView, DetailView

from .models import Recipe


class RecipeListView(ListView):
    """ Recipe ListView class. """
    model = Recipe
    template_name = 'recipes/index.html'
    context_object_name = 'posts'


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'
    context_object_name = 'recipe'
