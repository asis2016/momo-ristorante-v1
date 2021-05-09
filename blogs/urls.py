from django.urls import path

from . import views

urlpatterns = [
    path('<uuid:id>', views.blog_detail, name='blog_detail'),
    path('', views.blogs, name='blog'),
]
