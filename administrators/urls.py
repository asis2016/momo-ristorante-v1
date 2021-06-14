from django.urls import path

from blogs.views import DashboardBlogCreateView, DashboardBlogListView, DashboardBlogDetailView
from .views import AdministratorDashboard

urlpatterns = [

    # Blog
    path('blog/', DashboardBlogListView.as_view(), name='blog_list'),
    path('blog/<uuid:pk>/', DashboardBlogDetailView.as_view(), name='blog_detail'),

    path('blog/create/', DashboardBlogCreateView.as_view(), name='blog_create'),
    path('', AdministratorDashboard.as_view(), name='index')
]
