from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from apps.user_accounts.models import User
from apps.blog.models import Blog, Post
from apps.following.models import Follow


#site view is in no_user/views.py

def mini_site(request):
  selected_user = request.GET['clicked_user']
  user = User.objects.get_by_username(selected_user)
  blog = Blog.objects.get_blog_user(user)
  latest_posts = Post.objects.order_by_date(blog=blog)[:10]

  response = {
    'html': [],
  }

  try:
    Follow.objects.get_following(request.user, blog)
    follow = 'True'
  except:
    follow = 'False'

  url = request.META['HTTP_HOST']
  split_url = url.split('.')

  if split_url[0] == 'www':
    split_url.pop(0)
    domain_url = '.'.join(split_url)
  else:
    domain_url = url

  response['html'].append(render_to_string(
    'sites/mini_site.html',
    {
      'current_user': request.user,
      'blog_im_viewing_user': user,
      'viewing_blog': blog,
      'site_posts': latest_posts,
      'domain_url': domain_url,
      'follow': follow,
    }
  ))

  post_loop = Post.objects.render_posts(latest_posts, 'post.html', user=request.user, section='mini')
  response['post_html'] = post_loop

  return JsonResponse(response)

def get_ten_posts(request):
  site_user = request.GET['site_user']
  post_count = int(request.GET['post_count'])
  posts = Post.objects.ten_more_posts(post_count, ajax_user=site_user)

  response = {}

  try:
    mini = request.GET['mini']
    section = 'mini'
  except:
    section = 'site'

  post_loop = Post.objects.render_posts(posts, 'post.html', user=request.user, section=section)

  response['html'] = post_loop

  return JsonResponse(response)
