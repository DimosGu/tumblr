from django.shortcuts import render
from apps.blog.models import Post
from random import randint

def error404(request):
  pk_list = [1, 2]
  error_images = Post.objects.filter_by_pk(pk_list)
  context = {}
  context['section'] = 'error'
  context['page_title'] = 'Not found.'

  try:
    context['recent_img_post'] = error_images[randint(0, 4)]
  except:
    context['recent_img_post'] = None

  return render(request, '404.html', context)