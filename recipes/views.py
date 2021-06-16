"""
    recipes/views.py
    ----------------
"""
from django.urls import reverse_lazy
from django.views.generic import (CreateView,
                                  ListView,
                                  DetailView,
                                  UpdateView,
                                  DeleteView)

from .models import Recipe


class RecipeListView(ListView):
    """
    Recipe ListView class.
    """
    model = Recipe
    template_name = 'recipes/list.html'
    context_object_name = 'posts'


class RecipeDetailView(DetailView):
    """
    Recipe DetailView to display recipe details.
    """
    model = Recipe
    template_name = 'recipes/detail.html'
    context_object_name = 'recipe'


# C
class DashboardRecipeCreateView(CreateView):
    """
    The Recipe CreateView for the Dashboard.
    """
    model = Recipe
    template_name = 'recipes/dashboard/create.html'
    fields = ('title', 'image_url', 'excerpt', 'content',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# R
class DashboardRecipeListView(ListView):
    """
    The Recipe ListView for the Dashboard.
    """
    model = Recipe
    template_name = 'recipes/dashboard/list.html'
    context_object_name = 'recipes'


class DashboardRecipeDetailView(DetailView):
    """
    The Recipe DetailView for the Dashboard.
    """
    model = Recipe
    template_name = 'recipes/dashboard/detail.html'
    context_object_name = 'recipe'


class DashboardRecipeUpdateView(UpdateView):
    """
    The Recipe UpdateView for the Dashboard.
    """
    model = Recipe
    template_name = 'recipes/dashboard/update.html'
    fields = ('title', 'image_url', 'excerpt', 'content',)
    context_object_name = 'recipe'


class DashboardRecipeDeleteView(DeleteView):
    """
    The Recipe DeleteView for the Dashboard.
    """
    model = Recipe
    template_name = 'recipes/dashboard/delete.html'
    context_object_name = 'recipe'
    success_url = reverse_lazy('dashboard:recipe_list')
