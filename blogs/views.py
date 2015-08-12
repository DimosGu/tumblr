from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from blogs.forms import TextPostForm, PhotoPostForm
from blogs.models import Blog, Post
from user_accounts.models import User
from django.core.files import File

@login_required
def blog_edit(request, username):
	user = User.objects.get(username=username)
	blog = Blog.objects.get(user=user)
	posts = Post.objects.filter(blog=blog)
	latest_posts = posts.order_by('-pub_date')

	return render(request, 'blogs/blog_edit.html', {'latest_posts': latest_posts})

def delete_post(request):
	
	if request.method == 'POST':
		post = Post.objects.get(user=request.user, pk=request.POST.get('post_id')).delete()
		return HttpResponse('')

def post_text(request):

	if request.method == 'POST':
		text_form = TextPostForm(request.POST)

		if request.POST.get('post_edit_id'):
			post_edit = Post.objects.get(user=request.user, pk=request.POST.get('post_edit_id'))
			post_edit.title = request.POST.get('title')
			post_edit.text = request.POST.get('text')
			post_edit.tags = request.POST.get('tags')
			post_edit.save()

		elif text_form.is_valid():
			text_form.instance.user = request.user
			text_form.instance.blog = Blog.objects.get(user=request.user)
			text_form.save()

	return HttpResponse('')

def post_photo(request):

	if request.method == 'POST':
		photo_form = PhotoPostForm(request.POST, request.FILES)

		if request.POST.get('post_edit_id'):
			post_edit = Post.objects.get(user=request.user, pk=request.POST.get('post_edit_id'))
			post_edit.text = request.POST.get('text')
			post_edit.tags = request.POST.get('tags')

			if request.FILES:
				post_edit.file = request.FILES.get('file')

			post_edit.save()

		elif photo_form.is_valid():
			photo_form.instance.user = request.user
			photo_form.instance.blog = Blog.objects.get(user=request.user)
			photo_form.save()

	return HttpResponse('')
