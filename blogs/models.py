"""
    blogs/model.py
    --------------
    Blog consists of many articles.
    A blog is created by an Employee (employees.models) and it is publicly visible.
"""
import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Blog(models.Model):
    """
    Blog model as of v.1.0
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    excerpt = models.TextField(max_length=200, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='', default='default.png', blank=True)
    create_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])
