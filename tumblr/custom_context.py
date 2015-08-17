from blog.forms import TextPostForm, PhotoPostForm
from blog.models import Blog, Post
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

def header_forms(request):
	text_form = TextPostForm()
	photo_form = PhotoPostForm()

	post_forms = {
		'text_form': text_form,
		'photo_form': photo_form
	}
	
	return post_forms