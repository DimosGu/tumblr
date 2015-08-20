from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from user_accounts.models import User
from django.core.files import File
from .models import Blog, Post, Follow
from .forms import TextPostForm, PhotoPostForm

@login_required
def blog_edit(request, username):
	blog = Blog.objects.get(user=request.user)
	posts = Post.objects.filter(blog=blog)
	latest_posts = posts.order_by('-pub_date')[:10]

	context = {
		'latest_posts': latest_posts
	}

	return render(request, 'blog/blog_edit.html', context)

def follow(request):

	if request.method == 'POST':
		username = request.POST.get('username') 
		user_to_follow = User.objects.get(username=username)
		blog = Blog.objects.get(user=user_to_follow)
		follow = Follow(user=request.user, blog=blog)

		follow.save()

		response = {
			'username': username,
		}

		return JsonResponse(response)

def unfollow(request):

	if request.method == 'POST':
		username = request.POST.get('username') 
		user_to_unfollow = User.objects.get(username=username)
		blog = Blog.objects.get(user=user_to_unfollow)
		unfollow = Follow.objects.get(blog=blog)

		unfollow.delete()

		response = {
			'username': username,
		}

		return JsonResponse(response)

def get_more_posts(request):
	post_count = int(request.GET.get('post_count'))
	end_count = post_count + 10
	blog = Blog.objects.get(user=request.user)
	posts = Post.objects.filter(blog=blog).order_by('-pub_date')[post_count:end_count]

	response = {
		'html': [],
	}

	for post in posts:
		response['html'].append(render_to_string(
			'blog/blog_post.html',
			{
				'post': post,
				'user': request.user,
				'blog': blog,
			}
		))

	return JsonResponse(response)


def delete_post(request):
	
	if request.method == 'POST':
		post = Post.objects.get(user=request.user, pk=request.POST.get('post_id')).delete()

		return HttpResponse('delete success')

def edit_post(request):

	if request.method == 'POST':
		post_edit = Post.objects.get(user=request.user, pk=request.POST.get('post_edit_id'))

		post_edit.text = request.POST.get('text')
		post_edit.tags = request.POST.get('tags')
		
		if request.POST.get('title'):
			post_edit.title = request.POST.get('title')
		else:
			post_edit.title = ""
			
		if request.FILES:
			post_edit.file = request.FILES.get('file')
		
		post_edit.save()

		post = Post.objects.get(user=request.user, pk=request.POST.get('post_edit_id'))

		json_data = {
			'id_data': post.id,
			'text_data': post.text,
			'tags_data': post.tags,
			'title_data': post.title
		}

		if post.file:
			json_data['file_data'] = post.file.url

		return JsonResponse(json_data)

def post_text(request):

	if request.method == 'POST':
		text_form = TextPostForm(request.POST)

		if text_form.is_valid():
			text_form.instance.user = request.user
			text_form.instance.blog = Blog.objects.get(user=request.user)
			form_instance = text_form.save()

			post = Post.objects.get(user=request.user, pk=form_instance.pk)
			blog = Blog.objects.get(user=request.user)

			response = {
				'html': [],
			}

			response['html'].append(render_to_string(
				'blog/blog_post.html',
				{
					'post': post,
					'user': request.user,
					'blog': blog,
				}
			))

		return JsonResponse(response)

def post_photo(request):

	if request.method == 'POST':
		photo_form = PhotoPostForm(request.POST, request.FILES)

		if photo_form.is_valid():
			photo_form.instance.user = request.user
			photo_form.instance.blog = Blog.objects.get(user=request.user)
			form_instance = photo_form.save()

			post = Post.objects.get(user=request.user, pk=form_instance.pk)
			blog = Blog.objects.get(user=request.user)
			
			response = {
				'html': [],
			}

			response['html'].append(render_to_string(
				'blog/blog_post.html',
				{
					'post': post,
					'user': request.user,
					'blog': blog,
				}
			))

			return JsonResponse(response)
