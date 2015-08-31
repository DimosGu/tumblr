from django.db import models
from django.utils import timezone

class BaseManager(models.Manager):

  def order_by_date(self, blog=False, user=False):

    if user:
      return self.exclude(user=user).order_by('-pub_date')
    else:
      return self.filter(blog=blog).order_by('-pub_date')

class BaseModel(models.Model):

  pub_date = models.DateTimeField('pub date', default=timezone.now)
  objects = BaseManager()

  class Meta:
    abstract = True
