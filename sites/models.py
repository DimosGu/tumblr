from django.db import models
from blog.models import Blog
from user_accounts.models import User

class Site(models.Model):
	user = models.ForeignKey(User)
	domain = models.CharField(max_length=255, default=None)