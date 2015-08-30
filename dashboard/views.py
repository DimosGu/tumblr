from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import RequestContext
from django.template.loader import render_to_string
from blog.models import Blog, Post, Follow
from user_accounts.models import User

@login_required
def dashboard(request):

  latest_posts = Post.objects.sort_following_posts(request.user, 0)

  context = {
    'latest_posts': latest_posts
  }

  return render(request, 'dashboard/dashboard.html', context)

def get_ten_posts(request):

  response = {}
  post_count = int(request.GET['post_count'])
  latest_posts = Post.objects.sort_following_posts(request.user, post_count)
  appended_posts = Post.objects.loop_posts(latest_posts, 'dashboard/dashboard_post.html')
  response['html'] = appended_posts

  return JsonResponse(response)
