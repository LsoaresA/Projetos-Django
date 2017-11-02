from django.shortcuts import render, redirect
from django.http import HttpResponse

def cadastro(request):
	return render(request, 'cadastro.html')

def cadastro_page(request, num='01'):
	return render(request, 'pages.html')
