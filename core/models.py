from core.validators import validate_blog
from django.db import models
from django.contrib.auth import get_user_model

class Authorable(models.Model):
    """
    An abstract base class model that provides self-author ``author`` field.
    """
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True, blank=True)
    modified = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        abstract = True


class Titleable(models.Model):
    """
    An abstract base class model that provides title ``title`` char field with max length of 100.
    """
    title = models.CharField(max_length=150)

    class Meta:
        abstract = True


class BlogTitleAbstractModel(models.Model):
    title = models.CharField(max_length=150, validators=[validate_blog])

    class Meta:
        abstract = True
