from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Tags
from blog.models import Post


def search(request):
  if request.GET['tags_search']:
    print(request)
    return HttpResponseRedirect('/search/%s' % request.GET['tags_search'])
  else:
    return HttpResponseRedirect('/explore/recent')

def results(request, results):
  search_result = Tags.objects.get_tag(results)
  posts = search_result.post.exclude(user=request.user)[:10]
  context = Post.objects.combine_tags_posts(posts, user=request.user, follow=True)
  context['search'] = 'data=%s' % results

  return render(request, 'explore/explore.html', context)

def get_ten_posts(request, results):
  post_count = int(request.GET['post_count'])
  search_result = Tags.objects.get_tag(results)
  posts = Post.objects.ten_more_posts(post_count, user=request.user, search=search_result)

  appended_posts = Post.objects.loop_posts(
    posts, 'explore/explore_post.html', explore=True
  )

  response = {}
  response['html'] = appended_posts

  return JsonResponse(response)