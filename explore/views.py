from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import Blog, Post, Follow
from django.contrib.auth.decorators import login_required

@login_required
def explore(request):
	return HttpResponseRedirect('trending')

@login_required	
def trending(request):
	posts = Post.objects.all()
	latest_posts = posts.exclude(user=request.user).order_by('-pub_date')[:4]

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