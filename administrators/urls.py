from django.urls import path

from blogs.views import BlogCreateView

urlpatterns = [
    path('blog/create/', BlogCreateView.as_view(), name='blog_create')
]
