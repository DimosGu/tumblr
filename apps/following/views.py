from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Follow
from apps.user_accounts.models import User
from apps.blog.models import Blog, Post


@login_required
def following(request):
  context = {}

  following = Follow.objects.get_all_following(request.user)

  context['following'] = following
  context['section'] = 'following'
  context['page_title'] = 'Following | Tumblr'

  return render(request, 'following.html', context)


@login_required
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


@login_required
@csrf_exempt
def unfollow(request):

  if request.method == 'POST':
    username = request.POST.get('username')
    user_to_unfollow = User.objects.get_by_username(username)
    blog = Blog.objects.get_blog_user(user_to_unfollow)

    response = {}

    unfollow = Follow.objects.follow_filter(request.user, blog)
    unfollow.delete()
    response['username'] = username

    return JsonResponse(response)