from django.db import models
from django.conf import settings

class Blog(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	title = models.CharField(max_length=50, default="Untitled")

	def __str__(self):
		return self.title

class Post(models.Model):
	blog = models.ForeignKey(Blog)
	title = models.TextField()
	text = models.TextField()
	tags = models.TextField()

	def __str__(self):
		return self.title
