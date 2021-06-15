import debug_toolbar
from django.urls import path, include

from . import views

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    path('blog/', include('blogs.urls')),

    # contact
    path(r'^contact/', include('contact.urls')),
 
    # recipe
    path('recipe/', include('recipes.urls')),




    path('our-story.html', views.story, name='story'),
    path('reference.html', views.reference, name='references'),
    path('under-construction.html', views.underconstruction, name="under_construction"),
    path('', views.home, name='home'),

    #path('__debug__/', include(debug_toolbar.urls)),

]
