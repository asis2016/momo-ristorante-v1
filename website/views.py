"""
    website/views.py
    ================
    Main entry view for 'public'.
"""
from blogs.models import Blog
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from recipes.models import Recipe

from .models import Homepage, Setting


def datas():
    """
    Returns data for home.
    Read the documentation for the :meth: `home` method.
    """
    data = {
        "blog": Blog.objects.all()[:3],
        "recipes": Recipe.objects.all()[:8],
        'featurette': Homepage.objects.get(pk='featurette'),
        "homepage": Homepage.objects.all(),
        "jumbotron": Homepage.objects.get(pk='jumbotron'),
        "setting": Setting.objects.get(pk=1),
    }
    return data


class AboutView(TemplateView):
    """ Return about page. """

    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        posts = [
            {'title': 'Flabio Gustava', 'image': 'about-3.png'},
            {'title': 'Maria Smith', 'image': 'about-2.png'},
            {'title': 'Johnny Harris', 'image': 'about-1.png'}
        ]
        return {'posts': posts}





def contact(request):
    """ Return a contact page. """
    return render(request, 'contact/contact.html')


def home(request):
    """ Return render or HttpResponse for website > home. """
    return render(request, "website/index.html", datas())


def my_account(request):
    """ todo my account page with quick stat. """
    if request.is_authenticated:
        return HttpResponse('Yo this is my account. Quick stat page.')
    else:
        return HttpResponse('You are not authorized.')


def recipe(request):
    """ Return gallery arhive. """
    posts = Recipe.objects.all()
    return render(request, 'recipes/recipe.html', {
        'posts': posts
    })


def recipe_detail(request, id):
    """ Return single page for a gallery. """
    recipe = get_object_or_404(Recipe, pk=id)
    return render(request, 'recipes/detail.html', {
        'recipe': recipe
    })


def reference(request):
    """ Return all external references used for the developing this project. """
    return render(request, 'references/reference.html', datas())


def story(request):
    """ Return Our story page. """
    return render(request, 'story/our-story.html')


def underconstruction(request):
    """ Return "not developed" pages. """
    return render(request, 'under_construction/under_construction.html')

# def contact(request, id):
#    return HttpResponse('Yo this is contact page ' + str(id))
