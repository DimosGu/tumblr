from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from apps.blog.models import Blog


def settings(request):

  return HttpResponseRedirect(reverse('blog_appearance', args=[request.user.username]))

def blog_appearance(request, username):

  if username != request.user.username:
    return HttpResponseRedirect(reverse('blog_appearance', args=[request.user.username]))

  blog = Blog.objects.get_blog_user(request.user)

  context = {
    'section': 'blog-appearance',
    'page_title': 'Blog Settings',
    'logged_user': request.user,
    'viewing_user': request.user,
    'viewing_blog': blog,
  }

  return render(request, 'blog_appearance.html', context)