from django.db import models
from django.conf import settings
from django.utils import timezone

class Blog(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	title = models.CharField(max_length=50, default="Untitled")
	img = models.ImageField(upload_to='post_media', default='/media/default_blog_img.png')

	def __str__(self):
		return self.title

class Post(models.Model):
	blog = models.ForeignKey(Blog)
	pub_date = models.DateTimeField('date published', default=timezone.now)
	title = models.TextField(blank=True)
	text = models.TextField(blank=True)
	tags = models.TextField(blank=True)
	file = models.FileField(upload_to='post_media', blank=True)

	def __str__(self):
		if self.title != "":
			self.title
		elif self.file != "":
			self.title = 'File'
		else:
			self.title = 'Untitled'
		
		return self.title