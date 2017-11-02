from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^', include('home.urls', namespace='home')),
	url(r'^pages/', include('register.urls', namespace='register')),
    url(r'^admin/', admin.site.urls),
]
