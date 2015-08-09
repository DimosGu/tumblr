from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.core.context_processors import csrf
from user_accounts.forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login
from django.core import validators
from blogs.models import Blog, Post
from random import randint

def register(request):
	recent_img_post = Post.objects.exclude(file='').order_by('pub_date').reverse()[randint(0,4)]

	if request.user.is_authenticated():
		return HttpResponseRedirect('/dashboard')
	elif request.method == 'POST':
		form = RegistrationForm(request.POST)
		
		user_info = authenticate(
			email=request.POST['email'].lower(),
			password=request.POST['password']
		)

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

	context = {
		'form': form,
		'recent_img_post': recent_img_post
	}

	return render(request, 'no_user/register.html', context)

def check_fields(request):

	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		error = form.errors
		return JsonResponse(error)

def user_login(request):
	recent_img_post = Post.objects.exclude(file='').order_by('pub_date').reverse()[randint(0,4)]

	if request.user.is_authenticated():
		return HttpResponseRedirect('/dashboard')
	elif request.method == 'POST':
		form = LoginForm(request.POST)
		
		if form.is_valid():
			user_info = authenticate(
				email=form.cleaned_data['email'],
				password=form.cleaned_data['password']
			)
			login(request, user_info)
			return HttpResponseRedirect('/dashboard')

	else:
		form = LoginForm()

	context = {
		'form': form,
		'recent_img_post': recent_img_post
	}

	return render(request, 'no_user/login.html', context)