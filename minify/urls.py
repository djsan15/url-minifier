from django.conf.urls import include, url, patterns
from . import views


urlpatterns = patterns('',
	url(r'^$', views.HomeView.as_view(), name='home'),
	url(r'^(?P<short_url>[0-9A-Za-z]{1,30})/$', views.RedirectView.as_view(), name='redirect'),
	)