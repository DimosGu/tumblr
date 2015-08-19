from django.db import models
from django.conf import settings
from django.utils import timezone

def upload_path(instance, filename):
	return 'user_media/%s/%s' % (instance.user.username, filename)

class Blog(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	title = models.CharField(max_length=50, default="Untitled")
	img = models.ImageField(upload_to=upload_path, default='/media/default_blog_img.png')

	def __str__(self):
		return self.title

class Post(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	blog = models.ForeignKey(Blog)
	pub_date = models.DateTimeField('date published', default=timezone.now)
	title = models.TextField(blank=True)
	text = models.TextField(blank=True)
	tags = models.TextField(blank=True)
	file = models.FileField(upload_to=upload_path, blank=True)

	def __str__(self):		
		if self.title != "":
			return self.title
		elif self.file != "":
			return 'File'
		else:
			return 'Untitled'
		
class Follow(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	blog = models.ForeignKey(Blog)
	following_since = models.DateTimeField('following since', default=timezone.now)

	def __str__(self):
		return self.blog
