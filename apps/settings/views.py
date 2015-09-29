from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, JsonResponse
from apps.blog.models import Blog
from .forms import BlogEditForm


def settings(request):

  return HttpResponseRedirect(reverse('blog_appearance', args=[request.user.username]))

def blog_appearance(request, username):

  if username != request.user.username:
    return HttpResponseRedirect(reverse('blog_appearance', args=[request.user.username]))

  blog = Blog.objects.get_blog_user(request.user)

  context = {
    'section': 'blog-appearance',
    'page_title': 'Blog Settings',
    'current_user': request.user,
    'blog_im_viewing_user': request.user,
    'viewing_blog': blog,
    'blog_form': BlogEditForm,
  }

  return render(request, 'blog_appearance.html', context)

def edit_blog(request):

  if request.method == 'POST':
    blog_pk = request.POST['blog_pk']
    blog = Blog.objects.get_blog_pk(blog_pk)

    try:
      header_img = request.FILES['header_img']
      blog.bg_img = header_img
    except:
      header_img = False

    try:
      avatar_img = request.FILES['avatar_img']
      blog.img = avatar_img
    except:
      avatar_img = False

    try:
      blog_title = request.POST['blog_title']
      blog.title = blog_title
    except:
      blog_title = False

    Blog.change_attributes(blog, new_title=blog_title, new_img=avatar_img, new_bg_img=header_img)

  response = {}

  return JsonResponse(response)