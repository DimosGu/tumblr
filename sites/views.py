from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from user_accounts.models import User
from blog.models import Blog, Post

def mini_site(request):
	selected_user = request.GET['clicked_user']
	user = User.objects.get(username=selected_user)
	blog = Blog.objects.get(user=user)
	posts = Post.objects.filter(blog=blog)
	latest_posts = posts.order_by('-pub_date')[:10]

	domain_url = request.META['HTTP_HOST']

	response = {
		'html': [],
		'post_html': [],

	}

	response['html'].append(render_to_string(
		'sites/mini_site.html',
		{
			'viewing_user': user,
			'viewing_blog': blog,
			'site_posts': latest_posts,
			'domain_url': domain_url,
		}
	))

	for post in latest_posts:
		response['post_html'].append(render_to_string(
			'sites/mini_post.html',
			{
				'post': post
			}
		))

	return JsonResponse(response)

def get_ten_posts(request):
	site_user = request.GET['site_user']
	post_count = int(request.GET['post_count'])
	end_count = post_count + 10

	user = User.objects.get(username=site_user)
	blog = Blog.objects.get(user=user)
	posts = Post.objects.filter(blog=blog).order_by('-pub_date')[post_count:end_count]
	
	response = {
		'html': [],
	}

	for post in posts:
		response['html'].append(render_to_string(
			'sites/sites_post.html',
			{
				'post': post,
			}
		))

	return JsonResponse(response)