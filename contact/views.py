from django.shortcuts import render
from django.views.generic import TemplateView

class ContactView(TemplateView):
    template_name = 'contact/index.html'

    def get_success_url(self):
        return reverse('contact:index')
