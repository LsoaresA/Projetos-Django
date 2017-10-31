from django.shortcuts import render, redirect
from cadastro.forms import CadastroForm

def cadastro(request):
	form = CadastroForm(request.POST or None)
	context = {'form': form}
	if request.method == 'POST':
		if form.is_valid():
			form.save()
		return redirect('entrar:login')
	return render(request, 'cadastro.html', context)