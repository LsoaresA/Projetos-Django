from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
	return render(request, 'index.html')

def url_redirect(request):
	return redirect('entrar:login')
