from django.db import models
from user_accounts.models import User

class PostText(models.Model):
	
	user = models.ForeignKey(User)
	title = models.TextField()
	text = models.TextField()
	tags = models.TextField()
