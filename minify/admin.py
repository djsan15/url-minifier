from django.contrib import admin
from minify.models import Domain, URLMinify

import uuid


class URLMinifyAdmin(admin.ModelAdmin):
	list_display=('short_url','long_url','short_url_domain','long_url_domain','date_added',)
	fields = ('short_url_domain','short_url','long_url_domain','long_url',)
	# def save_model(self, request, obj, form, change):
	# 	if change and ('short_url' in form.changed_data):
	# 		if obj.short_url == None or obj.short_url == '':
	# 			obj.short_url='EMPTY'
	# 	obj.save()

class DomainAdmin(admin.ModelAdmin):
	list_display = ('name',)

admin.site.register
admin.site.register(URLMinify, URLMinifyAdmin)
admin.site.register(Domain, DomainAdmin)
