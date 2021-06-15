from django.urls import path

from .views import RecipeListView, RecipeDetailView

urlpatterns = [
    path('<uuid:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('', RecipeListView.as_view(), name='recipe'),
]
