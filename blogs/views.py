"""
    blogs/views.py
    --------------
"""
from django.db import transaction
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView

from .models import Blog


def blog_list(request):
    """
    Returns blog list.
    """
    blog_posts = Blog.objects.all()
    return render(request, 'blogs/list.html', {
        'blog_posts': blog_posts
    })


def blog_detail(request, id):
    """
    Returns detail (single) page of a blog article.
    """
    blog_id = get_object_or_404(Blog, pk=id)
    return render(request, 'blogs/detail.html', {
        'blog': blog_id
    })


@transaction.non_atomic_requests
class BlogCreateView(CreateView):
    """
    todo authentication (mixin)
    Creates a blog post.
    """
    model = Blog
    template_name = 'blogs/create.html'
    fields = '__all__'
    