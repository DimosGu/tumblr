from django.shortcuts import render
from django.http import  HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from blog.models import Blog, Post, Follow

def explore(request):
  return HttpResponseRedirect('recent')

def recent(request):
  latest_posts = Post.objects.ten_more_posts(0, user=request.user, explore=True)
  context = Post.objects.combine_tags_posts(latest_posts, user=request.user, follow=True)

  return render(request, 'explore/explore.html', context)

def get_ten_posts(request):
  post_count = int(request.GET['post_count'])
  latest_posts = Post.objects.ten_more_posts(post_count, user=request.user, explore=True)

  response = {}

  appended_posts = Post.objects.loop_posts(
    latest_posts, 'explore/explore_post.html', explore=True
  )

  response['html'] = appended_posts

  return JsonResponse(response)
