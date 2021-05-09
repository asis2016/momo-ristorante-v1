"""
    blogs/model.py
    --------------
    Blog consists of many articles.
    A blog is created by an Employee (employees.models) and it is publicly visible.
"""
from django.db import models
from django.urls import reverse


class Blog(models.Model):
    """
    Blog model as of v.1.0
    """
    user = models.ForeignKey('auth.User',
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    excerpt = models.TextField(max_length=100, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='',
                              default='media/default.png',
                              blank=True)
    create_date = models.DateField(blank=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('admin_blog_detail', args=[str(self.id)])
