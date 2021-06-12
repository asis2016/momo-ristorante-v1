import uuid

from django.contrib.auth import get_user_model
from django.db import models


class Recipe(models.Model):
    """
    Recipe model as of v.1.0.
    """
    CATEGORY = (
        ('WS', 'Western'),
        ('TB', 'Tibetan'),
        ('NP', 'Nepalese')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    excerpt = models.TextField(max_length=200, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='', default='default.png', blank=True)
    image_url = models.CharField(max_length=200, blank=True)
    create_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
