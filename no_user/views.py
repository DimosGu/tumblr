from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.core.context_processors import csrf
from user_accounts.forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login
from django.core import validators

def register(request):

	if request.user.is_authenticated():
		return HttpResponseRedirect('/dashboard')

	elif request.method == 'POST':
		form = RegistrationForm(request.POST)
		user_info = authenticate(
			email=request.POST['email'].lower(),
			password=request.POST['password'])

		if user_info is not None:
			login(request, user_info)
			redirect_url = {'url': 'dashboard'}
			return JsonResponse(redirect_url)

		elif form.is_valid():
			form.save()
			user_info = authenticate(
				email=form.cleaned_data['email'], 
				password=form.cleaned_data['password'])
			login(request, user_info)
			redirect_url = {'url': 'dashboard'}
			return JsonResponse(redirect_url)

		else:
			error = form.errors
			return JsonResponse(error)

	else:
		form = RegistrationForm()

	return render(request, 'no_user/register.html', {'form': form})

def check_fields(request):

	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		error = form.errors
		return JsonResponse(error)

def user_login(request):

	if request.method == 'POST':
		form = LoginForm(request.POST)
		
		if form.is_valid():
			user_info = authenticate(email=form.cleaned_data['email'],
													password=form.cleaned_data['password'])
			login(request, user_info)
			return HttpResponseRedirect('/dashboard')

	else:
		form = LoginForm()

	return render(request, 'no_user/login.html', {'form': form})