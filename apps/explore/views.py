from django.shortcuts import render
from django.http import  HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from apps.blog.models import Post

def explore(request):
  return HttpResponseRedirect(reverse('recent'))

def recent(request):

  if request.user.is_authenticated():
    latest_posts = Post.objects.ten_more_posts(0, user=request.user, explore=True)
    context = Post.objects.combine_post_attributes(latest_posts, user=request.user, follow=True, like=True)
  else:
    latest_posts = Post.objects.ten_more_posts(0, explore=True)
    context = Post.objects.combine_post_attributes(latest_posts, follow=True, like=True)

  context['section'] = 'explore'
  context['page_title'] = 'Recent'


  return render(request, 'explore/explore.html', context)

def text(request):

  if request.user.is_authenticated():
    latest_posts = Post.objects.ten_more_posts(0, user=request.user, explore='text')
    context = Post.objects.combine_post_attributes(latest_posts, user=request.user, follow=True, like=True)
  else:
    latest_posts = Post.objects.ten_more_posts(0, explore='text')
    context = Post.objects.combine_post_attributes(latest_posts, follow=True, like=True)

  context['section'] = 'explore'
  context['sub_section'] = 'text'
  context['page_title'] = 'Text'


  return render(request, 'explore/explore.html', context)

def photo(request):

  if request.user.is_authenticated():
    latest_posts = Post.objects.ten_more_posts(0, user=request.user, explore='photo')
    context = Post.objects.combine_post_attributes(latest_posts, user=request.user, follow=True, like=True)
  else:
    latest_posts = Post.objects.ten_more_posts(0, explore='photo')
    context = Post.objects.combine_post_attributes(latest_posts, follow=True, like=True)

  context['section'] = 'explore'
  context['sub_section'] = 'photo'
  context['page_title'] = 'Photo'


  return render(request, 'explore/explore.html', context)

def get_ten_posts(request):
  post_count = int(request.GET['post_count'])
  url_domain = request.META['HTTP_HOST']

  try:
    sub_section = request.GET['sub_section']
  except:
    sub_section = False

  if sub_section == 'text':
    explore = 'text'
  elif sub_section == 'photo':
    explore = 'photo'
  else:
    explore = True

  if request.user.is_authenticated():
    latest_posts = Post.objects.ten_more_posts(post_count, user=request.user, explore=explore)
  else:
    latest_posts = Post.objects.ten_more_posts(post_count, explore=explore)

  response = {}

  appended_posts = Post.objects.render_posts(
    latest_posts, 'post.html', section='explore', domain=url_domain, user=request.user
  )

  response['html'] = appended_posts

  return JsonResponse(response)
