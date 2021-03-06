from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Blog, Post
from .forms import TextPostForm, PhotoPostForm
from apps.user_accounts.models import User
from apps.search.models import Tags
from apps.following.models import Follow


@login_required
def blog_edit(request, username):

  if username != request.user.username:
    domain = request.META['HTTP_HOST']

    return HttpResponseRedirect('http://%s.%s' % (username, domain))

  latest_posts = Post.objects.ten_more_posts(0, user=request.user)
  context = Post.objects.combine_post_attributes(latest_posts)
  context['section'] = 'blog'

  return render(request, 'blog_edit.html', context)


def get_more_posts(request):
  post_count = int(request.GET.get('post_count'))
  posts = Post.objects.ten_more_posts(post_count, user=request.user)

  response = {}

  appended_posts = Post.objects.render_posts(
    posts, 'post.html', section='blog_edit'
  )

  response['html'] = appended_posts
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

    domain = request.META['HTTP_HOST']

    json_data = {
      'id_data': post.id,
      'text_data': post.text,
      'tags_data': [],
      'title_data': post.title,
      'domain_url': domain
    }

    current_tags = Tags.objects.filter_by_post(post)

    for tag in current_tags:
      tag.post.remove(post)

    new_tags = request.POST['tags'].lower()
    Tags.objects.create_tags(new_tags, post)

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
