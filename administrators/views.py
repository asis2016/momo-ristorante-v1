from django.views import generic

from blogs.models import Blog
from recipes.models import Recipe


class AdministratorDashboard(generic.TemplateView):
    """
    The templateview for Administrator
    """
    template_name = 'administrators/Dashboard/index.html'

    def relative_frequency_model(self):
        """
        Custom stats
        :return: list of relative frequencies of respective models.
        """
        relative_frequency = [
            {
                'model': 'Blog',
                'total': 15
            },
            {
                'model': 'Recipe',
                'total': 50
            },
            {
                'model': 'Gallery',
                'total': 35
            }
        ]
        return relative_frequency

    def get_context_data(self, **kwargs):
        context = super(AdministratorDashboard, self).get_context_data(**kwargs)
        context['latest_five_blog'] = Blog.objects.all()[:5]
        context['latest_five_recipes'] = Recipe.objects.all()[:5]

        # relative_frequency_model()
        context['relative_frequency_model'] = self.relative_frequency_model()
        return context
