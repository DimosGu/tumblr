from blog.forms import TextPostForm, PhotoPostForm
from search.forms import SearchForm
from blog.models import Blog, Follow, Post
from sites.models import Site
from user_accounts.models import User

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