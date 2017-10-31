from django.conf.urls import url, include
from django.contrib import admin
from cadastro.views import cadastro

urlpatterns = [
	url(r'^cadastro/$', cadastro, name='cadastro'),
    url(r'^admin/', admin.site.urls),
]
