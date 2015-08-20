from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import RequestContext
from django.template.loader import render_to_string
from blog.models import Blog, Post, Follow
from user_accounts.models import User

@login_required
def dashboard(request):
	following = Follow.objects.filter(user=request.user)

	post_list = []

	for user_blog in following:
		user = User.objects.get(username=user_blog)
		blog = Blog.objects.get(user=user)
		posts = Post.objects.filter(blog=blog)

		for post in posts:
			post_list.append(post.id)

	latest_posts = Post.objects.filter(pk__in=post_list).order_by('-pub_date')[:10]

	context = {
		'latest_posts': latest_posts
	}

	return render(request, 'dashboard/dashboard.html', context) 

def get_ten_posts(request):
	post_count = int(request.GET['post_count'])
	end_count = post_count + 10
	following = Follow.objects.filter(user=request.user)

	post_list = []

	for user_blog in following:
		user = User.objects.get(username=user_blog)
		blog = Blog.objects.get(user=user)
		posts = Post.objects.filter(blog=blog)

		for post in posts:
			post_list.append(post.id)

	latest_posts = Post.objects.filter(pk__in=post_list).order_by('-pub_date')[post_count:end_count]

	response = {
		'html': [],
	}

	for post in latest_posts:
		response['html'].append(render_to_string(
			'dashboard/dashboard_post.html', 
			{'post': post}
		))

	return JsonResponse(response)