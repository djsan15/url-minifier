from django.contrib import admin
from minify.models import Domain, URLMinify


class URLMinifyAdmin(admin.ModelAdmin):
	list_display=('short_url','long_url','date_added')
 
class DomainAdmin(admin.ModelAdmin):
	list_display = ('name',)

admin.site.register
admin.site.register(URLMinify, URLMinifyAdmin)
admin.site.register(Domain, DomainAdmin)
