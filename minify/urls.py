from django.conf.urls import include, url, patterns
from . import views


urlpatterns = patterns('',
	url(r'^$', views.HomeView.as_view(), name='home'),
	)