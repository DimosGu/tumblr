from apps.blog.forms import TextPostForm, PhotoPostForm
from apps.search.forms import SearchForm
from apps.blog.models import Blog, Post
from apps.user_accounts.models import User
from apps.likes.models import Like
from apps.following.models import Follow

def blog(request):

	try:
		blog = Blog.objects.get(user=request.user)
	except Blog.DoesNotExist:
		create_blog = Blog(user=request.user)
		create_blog.save()
		blog = Blog.objects.get(user=request.user)
	except:
		blog = None

	return {'blog': blog}

def header_forms(request):
	search_form = SearchForm()
	text_form = TextPostForm()
	photo_form = PhotoPostForm()

	post_forms = {
		'search_form': search_form,
		'text_form': text_form,
		'photo_form': photo_form
	}

	return post_forms

def domain_url(request):
	url = request.META['HTTP_HOST']
	split_url = url.split('.')

	split_url.pop(0)
	domain_url = '.'.join(split_url)

	return { 'domain_url': domain_url }

def like_count(request):

	if request.user.is_authenticated():
		like_count = Like.objects.count_liked(request.user)
	else:
		like_count = None

	return { 'like_count': like_count }

def following_count(request):

	if request.user.is_authenticated():
		following_count = Follow.objects.count_following(request.user)
	else:
		following_count = None

	return { 'following_count': following_count }