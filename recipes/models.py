from django.contrib.auth.models import User
from django.db import models


class Recipe(models.Model):
    """ Recipe model as of v.1.0. """
    CATEGORY = (
        ('WS', 'Western'),
        ('TB', 'Tibetan'),
        ('NP', 'Nepalese')
    )
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=50, blank=True)
    content = models.TextField(blank=True)
    create_date = models.DateField(blank=True)
    image = models.ImageField(blank=True)
    image_url = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return str(self.title)
