from django.db import models
from blog.models import Blog
from user_accounts.models import User
from tumblr.base_model import BaseModel, BaseManager


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