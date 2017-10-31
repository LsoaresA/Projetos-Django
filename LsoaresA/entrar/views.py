from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def do_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home:index')
	return render(request, 'login.html')

def do_logout(request):
	logout(request)
	return redirect('entrar:login')
