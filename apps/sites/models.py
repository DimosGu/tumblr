from django.db import models
from tumblr.base_model import BaseModel, BaseManager
from apps.user_accounts.models import User
from apps.blog.models import Blog


class SiteManager(BaseManager):

  def get_site_domain(self, domain):
    return self.get(domain=domain)


class Site(BaseModel):
  user = models.ForeignKey(User)
  domain = models.CharField(max_length=255, default=None)
  objects = SiteManager()

  class Meta:
    app_label = 'sites'

  def __str__(self):
    return self.domain