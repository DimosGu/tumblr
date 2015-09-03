from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Tags
from blog.models import Post


def search(request):
  try:
    tags = request.GET['tags_search']
    return HttpResponseRedirect('/search/%s' % tags.replace(' ', '+'))
  except:
    return HttpResponseRedirect('/explore/recent')

def results(request, results):
  try:
    print(results)

    if request.user.is_authenticated():
      search_result = Tags.objects.posts_with_tags(results, 0, user=request.user)
    else:
      search_result = Tags.objects.posts_with_tags(results, 0)

    context = Post.objects.combine_tags_posts(search_result, user=request.user, follow=True)
    context['search'] = 'data=%s' % results
    context['result'] = results.replace('+', ' ').upper()

    domain_url = request.META['HTTP_HOST']
    context['domain_url'] = domain_url

  except:
    context = {}
    context['search'] = 'data=%s' % 'NoResults'
    context['result'] = results.replace('+', ' ').upper()

  return render(request, 'explore/explore.html', context)

def get_ten_posts(request, results):
  post_count = int(request.GET['post_count'])
  response = {}

  try:

    if request.user.is_authenticated():
      search_result = Tags.objects.posts_with_tags(results, post_count, user=request.user)
    else:
      search_result = Tags.objects.posts_with_tags(results, post_count)

    appended_posts = Post.objects.render_posts(
      search_result, 'explore/explore_post.html', explore=True
    )

    response['html'] = appended_posts

    return JsonResponse(response)
  except:
    response['html'] = []

    return JsonResponse(response)