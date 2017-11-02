from django.conf.urls import url
from django.contrib import admin
from register.views import cadastro, cadastro_page

urlpatterns = [
	url(r'^register/$', cadastro, name='cadastro'),
	url(r'^(?P<num>[01-90]+)/register/', cadastro_page, name='cadastro_page'),
]