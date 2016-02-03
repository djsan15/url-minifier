from django.shortcuts import render
from django.views.generic import TemplateView
from .models import URLMinify, Domain
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, Http404

class HomeView(TemplateView):
	template_name = 'homepage.html'


class RedirectView(TemplateView):
	def get (self, request, *args, **kwargs):
		try:
			urlminify = URLMinify.objects.get(short_url=kwargs['short_url'])
		except ObjectDoesNotExist:
			raise Http404
		if request.get_host() == str(urlminify.short_url_domain).split('/')[2]:	
			redirect_url = str(urlminify.long_url_domain) + '/' + urlminify.long_url
		else:
			raise Http404
		return HttpResponseRedirect(redirect_url)