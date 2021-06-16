import uuid

from django.db import models
from django.urls import reverse

from core.models import (Authorable,
                         Titleable,
                         TimeStampedModel)


class Recipe(Authorable, Titleable, TimeStampedModel):
    """
    Recipe model as of v.1.0.
    """
    CATEGORY = (
        ('WS', 'Western'),
        ('TB', 'Tibetan'),
        ('NP', 'Nepalese')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    excerpt = models.TextField(max_length=200, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='', default='default.png', blank=True)
    image_url = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('dashboard:recipe_detail', args=[str(self.id)])
