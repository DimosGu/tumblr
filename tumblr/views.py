from django.shortcuts import render
from apps.blog.models import Post
from random import randint

def error404(request):
  chosen_posts = [1, 8, 9, 12, 15, 18]
  rand_post = chosen_posts[randint(0, 5)]

  context = {}

  try:
    error_image = Post.objects.get_pk(rand_post)
    context['img_post'] = error_image
  except:
    context['img_post'] = None

  context['section'] = 'error'
  context['page_title'] = 'Not found.'


  return render(request, '404.html', context)