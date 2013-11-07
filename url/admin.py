from ****.url.models import ShortLinks
from django.contrib import admin

class ShortLinksAdmin(admin.ModelAdmin):
        list_display=('id','visitor_ip','date','long_url','short_url')

admin.site.register(ShortLinks,ShortLinksAdmin)

