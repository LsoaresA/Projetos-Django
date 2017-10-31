from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^', include('home.urls', namespace='home')),
	url(r'^', include('cadastro.urls', namespace='cadastro')),
	url(r'^', include('entrar.urls', namespace='entrar')),
    url(r'^admin/', admin.site.urls),
]
