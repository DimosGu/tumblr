from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.core import validators
from random import randint
from apps.user_accounts.forms import RegistrationForm, LoginForm
from apps.blog.models import Blog, Post
from apps.following.models import Follow
from apps.user_accounts.models import User

def site_or_register(request):

  if request.subdomain:
    user = User.objects.get_by_username(request.subdomain)
    blog = Blog.objects.get_blog_user(user)
    latest_posts = Post.objects.order_by_date(blog=blog)[:10]
    tagged_posts = Post.objects.combine_post_attributes(latest_posts, user=request.user, like=True)

    try:
      am_following = Follow.objects.get_following(request.user, blog)
      follow = 'true'
    except:
      follow = 'false'

    context = {
      'current_site': user,
      'current_blog': blog,
      'latest_posts': tagged_posts['latest_posts'],
      'follow': follow,
      'section': 'sites',
      'page_title': blog.title,
    }

    return render(request, 'sites/site.html', context)

  else:

    if request.user.is_authenticated():
      return HttpResponseRedirect(reverse('dashboard'))
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

    try:
      recent_img_post = Post.objects.exclude(file='').order_by('pub_date').reverse()[randint(0,4)]
    except:
      recent_img_post = None

    context = {
      'form': form,
      'img_post': recent_img_post,
      'section': 'register',
      'page_title': 'Sign up',
    }

    return render(request, 'no_user/register.html', context)

def check_fields(request):

  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    error = form.errors
    return JsonResponse(error)

def user_login(request):

  if request.user.is_authenticated():
    return HttpResponseRedirect(reverse('dashboard'))
  elif request.method == 'POST':
    form = LoginForm(request.POST)

    if form.is_valid():
      user_info = authenticate(
        email=form.cleaned_data['email'],
        password=form.cleaned_data['password']
      )
      login(request, user_info)
      return HttpResponseRedirect(reverse('dashboard'))

  else:
    form = LoginForm()

  try:
    recent_img_post = Post.objects.exclude(file='').order_by('pub_date').reverse()[randint(0,4)]
  except:
    recent_img_post = None

  context = {
    'form': form,
    'img_post': recent_img_post,
    'section': 'login',
    'page_title': 'Log in',
  }

  return render(request, 'no_user/login.html', context)
