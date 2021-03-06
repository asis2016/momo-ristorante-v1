"""
    blogs/views.py
    --------------
"""
from django.db import transaction
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic

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
        'post': blog_id
    })


@transaction.non_atomic_requests
class DashboardBlogCreateView(generic.CreateView):
    """
    todo authentication (mixin)
    Creates a blog post.
    """
    model = Blog
    template_name = 'blogs/dashboard/create.html'
    fields = ('title', 'image_url', 'excerpt', 'content',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DashboardBlogListView(generic.ListView):
    """
    Blog list view for dashboard.
    """
    model = Blog
    template_name = 'blogs/dashboard/list.html'
    fields = '_all_'
    context_object_name = 'blog'


class DashboardBlogDetailView(generic.DetailView):
    """
    The Blog DetailView for the Dashboard.
    """
    model = Blog
    template_name = 'blogs/dashboard/detail.html'
    context_object_name = 'post'


class DashboardBlogUpdateView(generic.UpdateView):
    """
    Blog post update
    """
    model = Blog
    template_name = 'blogs/dashboard/update.html'
    fields = '__all__'
    context_object_name = 'post'


class DashboardBlogDeleteView(generic.DeleteView):
    """
    Blog post delete.
    """
    model = Blog
    template_name = 'blogs/dashboard/delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('dashboard:blog_list')