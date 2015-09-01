from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from user_accounts.models import User
from django.core.files import File
from .models import Blog, Post, Follow
from search.models import Tags
from .forms import TextPostForm, PhotoPostForm
from django.views.decorators.csrf import csrf_exempt


@login_required
def blog_edit(request, username):

  if username != request.user.username:
    domain = request.META['HTTP_HOST']
    return HttpResponseRedirect('http://%s.%s' % (username, domain))

  latest_posts = Post.objects.ten_more_posts(0, user=request.user)
  tagged_posts = Post.objects.combine_tags_posts(latest_posts)

  return render(request, 'blog/blog_edit.html', tagged_posts)

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
    post = Post.objects.get_pk(request.POST['post_id']).delete()

    return HttpResponse('delete success')

def edit_post(request):

  if request.method == 'POST':
    post_edit = Post.objects.get_pk(request.POST['post_edit_id'])

    post_edit.text = request.POST['text']

    if request.POST.get('title'):
      post_edit.title = request.POST['title']
    else:
      post_edit.title = ""

    if request.FILES:
      post_edit.file = request.FILES['file']

    post_edit.save()

    post = Post.objects.get_pk(request.POST['post_edit_id'])

    json_data = {
      'id_data': post.id,
      'text_data': post.text,
      'tags_data': [],
      'title_data': post.title
    }

    current_tags = Tags.objects.filter_by_post(post)

    for tag in current_tags:
      tag.post.clear()

    new_tags = request.POST['tags']
    stripped_tags = new_tags.replace('#', '').strip()
    split_tags = stripped_tags.split(' ')

    for tag in split_tags:

      if tag == '':
        pass
      else:

        try:
          tags = Tags.objects.get_tag(tag)
          tags.post.add(post)
        except:
          tags = Tags(tags=tag)
          tags.save()
          tags.post.add(post)

    created_tags = Tags.objects.filter_by_post(post)

    for tag in created_tags:
      json_data['tags_data'].append(tag.tags)

    if post.file:
      json_data['file_data'] = post.file.url

    return JsonResponse(json_data)

def post_text(request):

  if request.method == 'POST':
    text_form = TextPostForm(request.POST)
    response = Post.objects.render_new_post(request.user, text_form)

    return JsonResponse(response)

def post_photo(request):

  if request.method == 'POST':
    photo_form = PhotoPostForm(request.POST, request.FILES)
    response = Post.objects.render_new_post(request.user, photo_form)

    return JsonResponse(response)
