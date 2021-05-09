"""
    website/models.py
    _________________
"""

from django.db import models


class Setting(models.Model):
    """ General settings of a website as of v.1.0. """

    site_name = models.CharField(max_length=100, default='MOMO Ristorante')
    site_url = models.TextField(max_length=100, default='http://127.0.0.1:8000/')
    site_description = models.CharField(max_length=200, default='Lorem ipsum ')
    users_can_register = models.BooleanField(default=0)
    admin_email = models.CharField(max_length=100, default='admin@email.com')
    mailserver_url = models.CharField(max_length=200, blank=True)
    mailserver_login = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return f"{self.siteurl}"


class Homepage(models.Model):
    """ Homepage settings as of v.1.0. """
    homepage_id = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=100, default='Section XYZ')
    subtitle = models.CharField(max_length=100, default='subtitle XYZ')
    content = models.TextField(default='subtitle XYZ', blank=True)
    link_url = models.CharField(max_length=100, default='link_url', blank=True)
    image = models.ImageField(upload_to='', default='default.png', blank=True)

    def __str__(self):
        return f'{self.homepage_id}'
