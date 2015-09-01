from django.db import models
from tumblr.base_model import BaseManager, BaseModel
from blog.models import Post

class TagsManager(BaseManager):

  def get_tag(self, tag):
    return self.get(tags=tag)

  def filter_by_post(self, post):
    return self.filter(post=post)

  def create_tags(self, new_tags, post):
    stripped_tags = new_tags.replace('#', '').strip()
    split_tags = stripped_tags.split(' ')

    for tag in split_tags:

      if tag == '':
        pass
      else:

        try:
          tags = Tags.objects.get_tag(tag)
          tags.post.add(post)
        except:
          tags = Tags(tags=tag)
          tags.save()
          tags.post.add(post)

class Tags(BaseModel):

  tags = models.CharField(max_length=20, blank=True)
  post = models.ManyToManyField(Post)
  objects = TagsManager()

  def __str__(self):
    return self.tags

  def clean(self):
    print('cleaning')
    self.tags = self.tags.strip('', '#')

