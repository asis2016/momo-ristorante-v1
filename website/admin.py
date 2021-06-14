from django.contrib import admin
from .models import Setting
from .models import Homepage

class HomepageAdmin(admin.ModelAdmin):
    list_display = ('homepage_id', 'title', 'link_url', )

admin.site.register(Setting)
admin.site.register(Homepage, HomepageAdmin)
