from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from user_accounts.models import User
from django.core import validators
from django.contrib.auth import authenticate

class LoginForm(forms.Form):

	email = forms.CharField(
		required=True,
		widget=forms.EmailInput(attrs = {
			'placeholder': 'Email',
			'tabindex': '1'
		}),

		error_messages = {
			'required': 'You forgot to enter your email!'
		}
	)

	password = forms.CharField(
		required=True,
		widget=forms.PasswordInput(attrs = {
			'placeholder': 'Password',
			'tabindex': '2'
		}),

		error_messages = {
			'required': 'You forgot to enter your password!'
		}
	)
	
	def clean_email(self):
		email = self.cleaned_data["email"].lower()
		return email

	def clean_password(self):
		password = self.cleaned_data["password"]
		return password

	def clean(self):
		email = self.cleaned_data.get("email")
		password = self.cleaned_data.get("password")
		user = authenticate(email=email, password=password)

		if not email and not password:
			raise forms.ValidationError(
				'You do have to fill this stuff out, you know.'
			)
		elif user is None and email and password:
			raise forms.ValidationError(
				'Your email or password were incorrect.'
			)
		return self.cleaned_data

class RegistrationForm(forms.ModelForm):

	email = forms.EmailField(
		widget=forms.EmailInput(attrs = {
			'placeholder': 'Email',
			'tabindex': '1'
		}),

		error_messages = {
			'unique': 'That Email address is already in use',
			'required': 'You forgot to enter your email address!',
			'invalid': 'That\'s not a valid email address. Please try again.'
		}
	)

	password = forms.CharField(
		widget=forms.PasswordInput(attrs = {
			'placeholder': 'Password',
			'tabindex': '2'
		}),

		error_messages = {
			'required': 'a password is required',
			'length': 'The password must be at least 8 characters.'
		}
	)

	username = forms.CharField(
		widget=forms.TextInput(attrs = {
			'placeholder': 'Username',
			'tabindex': '3',
			'autocomplete': 'off'
		}),

		error_messages = {
			'unique': 'Someone has already claimed the username',
			'required': 'You forgot to enter your Username!',
		}
	)

	class Meta:
	  model = User
	  fields = ("email", "password", "username")

	def clean_email(self):
		email = self.cleaned_data["email"].lower()
		return email

	def clean_password(self):
		password = self.cleaned_data.get("password")

		if len(password) <= 7:
			raise forms.ValidationError(
				self.fields['password'].error_messages['length']
			)

		return password     

	def clean_username(self):
		username = self.cleaned_data["username"].lower()
		return username


	def save(self, commit=True):
	  user = super(RegistrationForm, self).save(commit=False)
	  user.email = self.cleaned_data['email']
	  user.set_password(self.cleaned_data["password"])

	  if commit:
	  	user.save()

	  return user

class UserChangeForm(forms.ModelForm):
	password = ReadOnlyPasswordHashField()

	class Meta:
		model = User
		fields = ('email', 'password', 'is_active', 'is_admin')

	def clean_password(self):
		return self.initial['password']