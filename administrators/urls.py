from django.urls import path

from blogs.views import (DashboardBlogCreateView,
                         DashboardBlogListView,
                         DashboardBlogDetailView,
                         DashboardBlogUpdateView,
                         DashboardBlogDeleteView)
from bookings.views import (DashboardBookingListView,
                            DashboardBookingDetailView,
                            DashboardBookingDeleteView,
                            )
from recipes.views import (DashboardRecipeCreateView,
                           DashboardRecipeListView,
                           DashboardRecipeDetailView,
                           DashboardRecipeUpdateView,
                           DashboardRecipeDeleteView)
from .views import AdministratorDashboard

urlpatterns = [

    # Blog
    path('blog/create/', DashboardBlogCreateView.as_view(), name='blog_create'),
    path('blog/', DashboardBlogListView.as_view(), name='blog_list'),
    path('blog/<uuid:pk>/detail/', DashboardBlogDetailView.as_view(), name='blog_detail'),
    path('blog/<uuid:pk>/update/', DashboardBlogUpdateView.as_view(), name='blog_update'),
    path('blog/<uuid:pk>/delete/', DashboardBlogDeleteView.as_view(), name='blog_delete'),

    # Booking
    path('booking/', DashboardBookingListView.as_view(), name='booking_list'),
    path('booking/<uuid:pk>/detail/', DashboardBookingDetailView.as_view(), name='booking_detail'),
    path('booking/<uuid:pk>/delete/', DashboardBookingDeleteView.as_view(), name='booking_delete'),

    # Recipe
    path('recipe/create/', DashboardRecipeCreateView.as_view(), name='recipe_create'),
    path('recipe/', DashboardRecipeListView.as_view(), name='recipe_list'),
    path('recipe/<uuid:pk>/detail/', DashboardRecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/<uuid:pk>/update/', DashboardRecipeUpdateView.as_view(), name='recipe_update'),
    path('recipe/<uuid:pk>/delete/', DashboardRecipeDeleteView.as_view(), name='recipe_delete'),

    path('', AdministratorDashboard.as_view(), name='index')
]
