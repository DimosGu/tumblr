from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from blogs.forms import TextPostForm, PhotoPostForm
from blogs.models import Blog, Post
from user_accounts.models import User
from django.core.files import File

@login_required
def blog(request, username):
	user = User.objects.get(username=username)
	blog = Blog.objects.get(user=user)
	posts = Post.objects.all().filter(blog=blog)
	latest_posts = posts.order_by('-pub_date')

	return render(request, 'blogs/blog.html', {'latest_posts': latest_posts})

@login_required
def post_text(request):

	if request.method == 'POST':
		text_form = TextPostForm(request.POST)

		if text_form.is_valid():
			text_form.instance.blog = Blog.objects.get(user=request.user)
			text_form.save()

			return HttpResponse('')


@login_required
def post_photo(request):

	if request.method == 'POST':
		photo_form = PhotoPostForm(request.POST, request.FILES)

		if photo_form.is_valid():
			photo_form.instance.blog = Blog.objects.get(user=request.user)
			photo_form.save()

			return HttpResponse('')