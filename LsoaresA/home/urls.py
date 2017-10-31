from django.conf.urls import url, include
from django.contrib import admin
from home.views import index, url_redirect

urlpatterns = [
	url(r'^home/$', index, name='index'),
	url(r'^$', url_redirect, name='url_redirect'),
    url(r'^admin/', admin.site.urls),
]