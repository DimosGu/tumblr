from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from apps.blog.models import Post

@login_required
def dashboard(request):

  latest_posts = Post.objects.sort_following_posts(request.user, 0)
  context = Post.objects.combine_tags_posts(latest_posts)
  context['section'] = 'dashboard'

  return render(request, 'dashboard/dashboard.html', context)

def get_ten_posts(request):

  response = {}
  post_count = int(request.GET['post_count'])
  latest_posts = Post.objects.sort_following_posts(request.user, post_count)
  appended_posts = Post.objects.render_posts(latest_posts, 'post.html')
  response['html'] = appended_posts

  return JsonResponse(response)
