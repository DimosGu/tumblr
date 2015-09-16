from django.db import models
from tumblr.base_model import BaseManager, BaseModel
from apps.blog.models import Post
from apps.user_accounts.models import User


class LikeManager(BaseManager):

  def count_liked(self, user):
    return self.filter(user=user).count()

  def filter_like(self, user, post):
    return self.filter(user=user, post=post)

  def check_like(self, user, post):
    return self.get(user=user, post=post)

  def filter_order_all_liked(self, user, post_count):
    end_count = post_count + 10
    return self.filter(user=user).order_by('-pub_date')[post_count:end_count]


class Like(BaseModel):

  user = models.ForeignKey(User)
  post = models.ForeignKey(Post)
  objects = LikeManager()

  class Meta:
    app_label = 'likes'

  def __str__(self):
    return '%s --> %s' % (self.user, self.post.user)