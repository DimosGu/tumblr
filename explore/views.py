from django.shortcuts import render
from django.http import  HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from blog.models import Blog, Post, Follow

@login_required
def explore(request):
  return HttpResponseRedirect('recent')

@login_required
def recent(request):
  latest_posts = Post.objects.ten_more_posts(0, user=request.user, explore=True)

  context = {
    'latest_posts': [],
  }

  for post in latest_posts:
    blog = Blog.objects.get_blog_user(post.user)

    try:
      follow = Follow.objects.get_following(request.user, blog)
      context['latest_posts'].append((post, 'true'))
    except:
      context['latest_posts'].append((post, 'false'))

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
