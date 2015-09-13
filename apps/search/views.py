from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Tags
from apps.blog.models import Post


def search(request):

  try:
    tags = request.GET['tags_search']
    return HttpResponseRedirect('/search/%s' % tags.replace(' ', '+'))
  except:
    return HttpResponseRedirect(reverse('recent'))

def results(request, results):

  try:

    if request.user.is_authenticated():
      search_result = Tags.objects.posts_with_tags(results.lower(), 0, user=request.user)
    else:
      search_result = Tags.objects.posts_with_tags(results.lower(), 0)

    context = Post.objects.combine_tags_posts(search_result, user=request.user, follow=True)

    if not context['latest_posts']:
      context['search'] = 'data=%s' % 'NoResults'
    else:
      context['search'] = 'data=%s' % results.lower()

  except:
    context = {}
    context['search'] = 'data=%s' % 'NoResults'

  result = results.replace('+', ' ')

  context['result'] = result.upper()
  context['section'] = 'explore'
  context['page_title'] = '%s | Tumblr' % result

  return render(request, 'explore/explore.html', context)

def get_ten_posts(request, results):
  post_count = int(request.GET['post_count'])
  url_domain = request.META['HTTP_HOST']
  response = {}

  try:

    if request.user.is_authenticated():
      search_result = Tags.objects.posts_with_tags(results, post_count, user=request.user)
    else:
      search_result = Tags.objects.posts_with_tags(results, post_count)

    appended_posts = Post.objects.render_posts(
      search_result, 'post.html', explore_domain=url_domain, user=request.user
    )

    response['html'] = appended_posts

    if not response['html']:
      response['html'] = "NoResults"
      response['result'] = results.replace('+', ' ')
    else:
      pass

  except:
    response['error'] = 'no posts with those tags'

  return JsonResponse(response)