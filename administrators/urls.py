from django.urls import path

from blogs.views import (DashboardBlogCreateView,
                         DashboardBlogListView,
                         DashboardBlogDetailView,
                         DashboardBlogUpdateView,
                         DashboardBlogDeleteView)
from .views import AdministratorDashboard

urlpatterns = [

    # Blog
    path('blog/', DashboardBlogListView.as_view(), name='blog_list'),
    path('blog/<uuid:pk>/detail/', DashboardBlogDetailView.as_view(), name='blog_detail'),
    path('blog/<uuid:pk>/update/', DashboardBlogUpdateView.as_view(), name='blog_update'),
    path('blog/<uuid:pk>/delete/', DashboardBlogDeleteView.as_view(), name='blog_delete'),

    path('blog/create/', DashboardBlogCreateView.as_view(), name='blog_create'),
    path('', AdministratorDashboard.as_view(), name='index')
]
