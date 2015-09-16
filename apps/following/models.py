from django.db import models
from tumblr.base_model import BaseManager, BaseModel
from apps.blog.models import Blog
from apps.user_accounts.models import User


class FollowManager(BaseManager):

  def follow_filter(self, user, blog):
    return self.filter(user=user, blog=blog)

  def get_following(self, user, blog):
    return self.get(user=user, blog=blog)

  def count_following(self, user):
    return self.filter(user=user).count()

  def get_all_following(self, user):
    return self.filter(user=user).order_by('-pub_date')


class Follow(BaseModel):

  user = models.ForeignKey(User)
  blog = models.ForeignKey(Blog)
  objects = FollowManager()

  class Meta:
    app_label = 'following'

  def __str__(self):
    return self.blog.user.username