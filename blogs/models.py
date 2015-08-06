from django.db import models
from django.conf import settings
from django.utils import timezone

class Blog(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	title = models.CharField(max_length=50, default="Untitled")
	img = models.ImageField(upload_to='/media/', default='/media/default_blog_img.png')

	def __str__(self):
		return self.title

class Post(models.Model):
	blog = models.ForeignKey(Blog)
	pub_date = models.DateTimeField('date published', default=timezone.now)
	title = models.TextField()
	text = models.TextField()
	tags = models.TextField()

	def __str__(self):
		return self.title
