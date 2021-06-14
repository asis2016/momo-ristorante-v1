import debug_toolbar
from django.urls import path, include

from . import views

urlpatterns = [

    # blogs
    path('blog', include(('blogs.urls', 'blog'), namespace='blog')),

    # contact
    path(r'^contact/', include(('contact.urls', 'contact'), namespace='contact')),
 
    # recipe
    path('recipe', include('recipes.urls')),

    path('', views.home, name="home"),
    path('about/', views.AboutView.as_view(), name='about'),

    path('our-story.html', views.story, name='story'),
    path('reference.html', views.reference, name='references'),
    path('under-construction.html', views.underconstruction, name="under_construction"),

    #path('__debug__/', include(debug_toolbar.urls)),

]
