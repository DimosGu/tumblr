from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from user_accounts.models import User
from django.core.files import File
from .models import Blog, Post, Follow
from .forms import TextPostForm, PhotoPostForm
from django.views.decorators.csrf import csrf_exempt

@login_required
def blog_edit(request, username):

  if username != request.user.username:
    domain = request.META['HTTP_HOST']
    return HttpResponseRedirect('http://%s.%s' % (username, domain))

  latest_posts = Post.objects.ten_more_posts(0, user=request.user)

  context = {
    'latest_posts': latest_posts
  }

  return render(request, 'blog/blog_edit.html', context)

@csrf_exempt
def follow(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    user_to_follow = User.objects.get_by_username(username)
    blog = Blog.objects.get_blog_user(user_to_follow)

    response = {}

    try:
      follow = Follow.objects.get_following(request.user, blog)
      response['error'] = 'already following'
    except:
      follow = Follow(user=request.user, blog=blog)
      follow.save()
      response['username'] = username

    return JsonResponse(response)

@csrf_exempt
def unfollow(request):

  if request.method == 'POST':
    username = request.POST.get('username')
    user_to_unfollow = User.objects.get_by_username(username)
    blog = Blog.objects.get_blog_user(user_to_unfollow)

    response = {}

    try:
      unfollow = Follow.objects.get_following(request.user, blog)
      unfollow.delete()
      response['username'] = username
    except:
      response['error'] = 'no following object existed'

    return JsonResponse(response)

def get_more_posts(request):
  post_count = int(request.GET.get('post_count'))
  posts = Post.objects.ten_more_posts(post_count, user=request.user, return_fields=True)

  response = {
    'html': [],
  }

  for post in posts['filtered_posts']:
    response['html'].append(render_to_string(
      'blog/blog_post.html',
      {
        'post': post,
        'user': request.user,
        'blog': posts['blog'],
      }
    ))

  return JsonResponse(response)


def delete_post(request):

  if request.method == 'POST':
    post = Post.objects.get_by_user_pk(request.user, request.POST['post_id']).delete()

    return HttpResponse('delete success')

def edit_post(request):

  if request.method == 'POST':
    post_edit = Post.objects.get_by_user_pk(request.user, request.POST['post_edit_id'])

    post_edit.text = request.POST['text']
    post_edit.tags = request.POST['tags']

    if request.POST.get('title'):
      post_edit.title = request.POST['title']
    else:
      post_edit.title = ""

    if request.FILES:
      post_edit.file = request.FILES['file']

    post_edit.save()

    post = Post.objects.get_by_user_pk(request.user, request.POST['post_edit_id'])

    json_data = {
      'id_data': post.id,
      'text_data': post.text,
      'tags_data': post.tags,
      'title_data': post.title
    }

    if post.file:
      json_data['file_data'] = post.file.url

    return JsonResponse(json_data)

def post_text(request):

  if request.method == 'POST':
    text_form = TextPostForm(request.POST)

    if text_form.is_valid():
      text_form.instance.user = request.user
      text_form.instance.blog = Blog.objects.get_blog_user(request.user)
      form_instance = text_form.save()

      post = Post.objects.get_by_user_pk(request.user, form_instance.pk)
      blog = Blog.objects.get_blog_user(request.user)

      response = {
        'html': [],
      }

      response['html'].append(render_to_string(
        'blog/blog_post.html',
        {
          'post': post,
          'user': request.user,
          'blog': blog,
        }
      ))

    return JsonResponse(response)

def post_photo(request):

  if request.method == 'POST':
    photo_form = PhotoPostForm(request.POST, request.FILES)

    if photo_form.is_valid():
      photo_form.instance.user = request.user
      photo_form.instance.blog = Blog.objects.get_blog_user(request.user)
      form_instance = photo_form.save()

      post = Post.objects.get_by_user_pk(request.user, form_instance.pk)
      blog = Blog.objects.get_blog_user(request.user)

      response = {
        'html': [],
      }

      response['html'].append(render_to_string(
        'blog/blog_post.html',
        {
          'post': post,
          'user': request.user,
          'blog': blog,
        }
      ))

      return JsonResponse(response)
