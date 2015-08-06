from blogs.forms import TextPostForm, PhotoPostForm
from user_accounts.models import User
from blogs.models import Blog, Post

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
	
	return {'text_form': text_form, 'photo_form': photo_form}