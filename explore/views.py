from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from blog.models import Blog, Post, Follow

@login_required
def explore(request):
	return HttpResponseRedirect('recent')

@login_required	
def recent(request):
	posts = Post.objects.all()
	latest_posts = posts.exclude(user=request.user).order_by('-pub_date')[:10]

	context = {
		'latest_posts': [],
	}

	for post in latest_posts:
		blog = Blog.objects.get(user=post.user)
		
		try:
			follow = Follow.objects.get(blog=blog)
		except: 
			follow = None

		if follow:
			context['latest_posts'].append((post, 'true'))
		else:
			context['latest_posts'].append((post, 'false'))

	return render(request, 'explore/explore.html', context)

def get_ten_posts(request):
	post_count = int(request.GET['post_count'])
	end_count = post_count + 10
	posts = Post.objects.all()
	latest_posts = posts.exclude(user=request.user).order_by('-pub_date')[post_count:end_count]

	response = {
		'html': [],
	}

	for post in latest_posts:
		blog = Blog.objects.get(user=post.user)
		
		try:
			follow = Follow.objects.get(blog=blog)
		except: 
			follow = None

		if follow:
			response['html'].append(render_to_string(
				'explore/explore_post.html',
				{
					'post': post,
					'following': 'true'
				}
			))

		else:
			response['html'].append(render_to_string(
				'explore/explore_post.html',
				{
					'post': post,
					'following': 'false'
				}
			))

	return JsonResponse(response)