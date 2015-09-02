from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Tags
from blog.models import Post


def search(request):
  if request.GET['tags_search']:
    return HttpResponseRedirect('/search/%s' % request.GET['tags_search'])
  else:
    return HttpResponseRedirect('/explore/recent')

def results(request, results):
  try:
    search_result = Tags.objects.get_tag(results)

    if request.user.is_authenticated():
      posts = search_result.post.exclude(user=request.user)[:10]
    else:
      posts = search_result.post.all()[:10]

    context = Post.objects.combine_tags_posts(posts, user=request.user, follow=True)
    context['search'] = 'data=%s' % results
    context['result'] = results.upper()

    domain_url = request.META['HTTP_HOST']
    context['domain_url'] = domain_url

  except:
    context = {}
    context['search'] = 'data=%s' % 'NoResults'
    context['result'] = results.upper()

  return render(request, 'explore/explore.html', context)

def get_ten_posts(request, results):
  post_count = int(request.GET['post_count'])
  response = {}

  try:
    search_result = Tags.objects.get_tag(results)

    if request.user.is_authenticated():
      posts = Post.objects.ten_more_posts(post_count, user=request.user, search=search_result)
    else:
      posts = Post.objects.ten_more_posts(post_count, search=search_result)

    appended_posts = Post.objects.loop_posts(
      posts, 'explore/explore_post.html', explore=True
    )

    response['html'] = appended_posts

    return JsonResponse(response)
  except:
    response['html'] = []

    return JsonResponse(response)