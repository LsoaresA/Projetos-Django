from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class CadastroForm(forms.ModelForm):
	User._meta.get_field('email').blank=False
	User._meta.get_field('username').blank=False
	User._meta.get_field('password').blank=False
	User._meta.get_field('is_staff').default=1
	class Meta:
		model = User
		fields = ['first_name','last_name','email','username','password']
		widgets = {
			'first_name': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255}),
			'last_name': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255}),
			'email': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'Email Address'}),
			'username': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'Username'}),
			'password': forms.PasswordInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'Password'}),
		}

	def save(self, commit=True):
		user = super(CadastroForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password'])
		if commit:
			user.save()
		return user