from django.shortcuts import render
from django.http import  HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from apps.blog.models import Blog, Post, Follow

def explore(request):
  return HttpResponseRedirect(reverse('recent'))

def recent(request):

  if request.user.is_authenticated():
    latest_posts = Post.objects.ten_more_posts(0, user=request.user, explore=True)
    context = Post.objects.combine_tags_posts(latest_posts, user=request.user, follow=True)
  else:
    latest_posts = Post.objects.ten_more_posts(0, explore=True)
    context = Post.objects.combine_tags_posts(latest_posts, follow=True)

  context['section'] = 'explore'
  context['page_title'] = 'Recent | Tumblr'


  return render(request, 'explore/explore.html', context)

def get_ten_posts(request):
  post_count = int(request.GET['post_count'])
  url_domain = request.META['HTTP_HOST']

  if request.user.is_authenticated():
    latest_posts = Post.objects.ten_more_posts(post_count, user=request.user, explore=True)
  else:
    latest_posts = Post.objects.ten_more_posts(post_count, explore=True)

  response = {}

  appended_posts = Post.objects.render_posts(
    latest_posts, 'post.html', explore_domain=url_domain, user=request.user
  )

  response['html'] = appended_posts

  return JsonResponse(response)
