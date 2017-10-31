from django.conf.urls import url
from django.contrib import admin
from entrar.views import do_login, do_logout

urlpatterns = [
	url(r'^entrar/$', do_login, name='login'),
	url(r'^sair/$', do_logout, name='logout'),
    url(r'^admin/', admin.site.urls),
]
