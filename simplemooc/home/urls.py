from django.conf.urls import url
from django.contrib import admin
from home.views import index, url_redirect

urlpatterns = [
	url(r'^$', url_redirect, name='url_redirect'),
	url(r'^home/$', index, name='index'),
]
