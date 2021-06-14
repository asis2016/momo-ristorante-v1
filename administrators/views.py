from django.shortcuts import render
from django.views import generic

class AdministratorDashboard(generic.TemplateView):
    """
    The templateview for Administrator
    """
    template_name = 'administrators/Dashboard/index.html'
