from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from blogs.forms import TextPostForm, PhotoPostForm
from django.template.loader import render_to_string
from blogs.models import Blog, Post
from user_accounts.models import User
from django.core.files import File

@login_required
def blog_edit(request, username):
	blog = Blog.objects.get(user=request.user)
	posts = Post.objects.filter(blog=blog)	
	latest_posts = posts.order_by('-pub_date')[:10]

	context = {
		'latest_posts': latest_posts
	}

	return render(request, 'blogs/blog_edit.html', context)

def get_more_posts(request):
	post_count = int(request.GET.get('post_count'))
	blog = Blog.objects.get(user=request.user)
	posts = Post.objects.filter(blog=blog).order_by('-pub_date')

	posts_to_json = {
		'post_0' : {},
		'post_1' : {},
		'post_2' : {},
		'post_3' : {},
		'post_4' : {},
		'post_5' : {},
		'post_6' : {},
		'post_7' : {},
		'post_8' : {},
		'post_9' : {}
	} 

	for x in range(0, 10):

		try:

			if posts[post_count].file:
				posts_to_json['post_%s' % x]['file_data'] = posts[post_count].file.url

			posts_to_json['post_%s' % x]['blog_img'] = blog.img.url
			posts_to_json['post_%s' % x]['username'] = request.user.username
			posts_to_json['post_%s' % x]['id_data'] = posts[post_count].pk
			posts_to_json['post_%s' % x]['title_data'] = posts[post_count].title
			posts_to_json['post_%s' % x]['text_data'] = posts[post_count].text
			posts_to_json['post_%s' % x]['tags_data'] = posts[post_count].tags

			post_count += 1
			
		except: 
			pass
					
	return JsonResponse(posts_to_json)


def delete_post(request):
	
	if request.method == 'POST':
		post = Post.objects.get(user=request.user, pk=request.POST.get('post_id')).delete()

		return HttpResponse('success')

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

			json_data = {
				'blog_img': blog.img.url,
				'username': request.user.username,
				'id_data': post.id,
				'title_data': post.title,
				'text_data': post.text,
				'tags_data': post.tags
			}

		return JsonResponse(json_data)

def post_photo(request):

	if request.method == 'POST':
		photo_form = PhotoPostForm(request.POST, request.FILES)

		if photo_form.is_valid():
			photo_form.instance.user = request.user
			photo_form.instance.blog = Blog.objects.get(user=request.user)
			form_instance = photo_form.save()

			post = Post.objects.get(user=request.user, pk=form_instance.pk)
			blog = Blog.objects.get(user=request.user)
			
			json_data = {
				'blog_img': blog.img.url,
				'username': request.user.username,
				'id_data': post.id,
				'file_data': post.file.url,
				'text_data': post.text,
				'tags_data': post.tags
			}

			return JsonResponse(json_data)
