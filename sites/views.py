from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from user_accounts.models import User
from blog.models import Blog, Post, Follow


#site view is in no_user/views.py

def mini_site(request):
  selected_user = request.GET['clicked_user']
  user = User.objects.get_by_username(selected_user)
  blog = Blog.objects.get_blog_user(user)
  latest_posts = Post.objects.order_by_date(blog=blog)[:10]
  domain_url = request.META['HTTP_HOST']

  response = {
    'html': [],
  }

  try:
    Follow.objects.get_following(request.user, blog)
    follow = 'true'
  except:
    follow = 'false'

  response['html'].append(render_to_string(
    'sites/mini_site.html',
    {
      'logged_user': request.user,
      'viewing_user': user,
      'viewing_blog': blog,
      'site_posts': latest_posts,
      'domain_url': domain_url,
      'follow': follow,
    }
  ))

  post_loop = Post.objects.render_posts(latest_posts, 'post.html', mini=True)
  response['post_html'] = post_loop

  return JsonResponse(response)

def get_ten_posts(request):
  site_user = request.GET['site_user']
  post_count = int(request.GET['post_count'])
  posts = Post.objects.ten_more_posts(post_count, ajax_user=site_user)

  response = {}

  try:
    mini = request.GET['mini']
  except:
    pass

  post_loop = Post.objects.render_posts(posts, 'post.html', mini=True)

  response['html'] = post_loop

  return JsonResponse(response)
