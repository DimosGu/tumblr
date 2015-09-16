from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Like
from apps.blog.models import Post


@login_required
def likes(request):

  liked_posts = Like.objects.filter_order_all_liked(request.user, 0)
  converted_posts = Post.objects.convert_liked_to_post(liked_posts)

  context = Post.objects.combine_post_attributes(converted_posts, user=request.user, follow=True, like=True)
  context['section'] = 'likes'
  context['page_title'] = 'Likes | Tumblr'

  return render(request, 'likes.html', context)


def ten_more_posts(request):
  post_count = int(request.GET['post_count'])
  response = {}

  liked_posts = Like.objects.filter_order_all_liked(request.user, post_count)
  converted_posts = Post.objects.convert_liked_to_post(liked_posts)
  appended_posts = Post.objects.render_posts(converted_posts, 'post.html', user=request.user, section='likes')

  response['html'] = appended_posts

  return JsonResponse(response)


@login_required
@csrf_exempt
def like(request):

  if request.method == 'POST':
    post_pk = request.POST['post_pk']
    post = Post.objects.get_pk(post_pk)

    response = {}

    try:
      like = Like.objects.check_like(request.user, post)
      response['status'] = 'already liking'
    except:
      like = Like(user=request.user, post=post)
      like.save()
      response['status'] = 'now liking'


    return JsonResponse(response)


@login_required
@csrf_exempt
def unlike(request):

  if request.method == 'POST':

    post_pk = request.POST['post_pk']
    post = Post.objects.get_pk(post_pk)

    like = Like.objects.filter_like(request.user, post)
    like.delete()

    response = {}
    response['status'] = 'no longer liking'

    return JsonResponse(response)