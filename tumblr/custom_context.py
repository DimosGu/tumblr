from apps.blog.forms import TextPostForm, PhotoPostForm
from apps.search.forms import SearchForm
from apps.blog.models import Blog, Post
from apps.sites.models import Site
from apps.user_accounts.models import User

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

def site(request):

	try:
		site = Site.objects.get(user=request.user)
	except Site.DoesNotExist:
		create_site = Site(user=request.user, domain=request.user.username)
		create_site.save()
		site = Site.objects.get(user=request.user)
	except:
		site = None

	return {'site': site}

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

	if split_url[0] == 'www':
		split_url.pop(0)
		domain_url = '.'.join(split_url)
	else:
		domain_url = url

	return { 'domain_url': domain_url }