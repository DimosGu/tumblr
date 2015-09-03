from django.db import models
from tumblr.base_model import BaseManager, BaseModel
from blog.models import Post

class TagsManager(BaseManager):

  def posts_with_tags(self, tags, post_count, user=False):
    end_count = post_count + 10

    tag_list = []
    split_tags = tags.replace('+', ' ').split(' ')

    for tag in split_tags:

      if tag == '':
        pass
      else:
        tagss = self.get(tags=tag)
        tag_list.append(tagss.pk)

    if user:
      post_with_tags = Post.objects.exclude(user=user)
    else:
      post_with_tags = Post.objects.all()

    for pk in tag_list:
      loop_posts = post_with_tags.filter(tags__pk=pk)
      post_with_tags = loop_posts

    ordered_posts = post_with_tags.order_by('-pub_date')[post_count:end_count]

    return ordered_posts

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
          tags = Tags.objects.get(tags=tag)
          tags.post.add(post)
        except:
          tags = Tags(tags=tag)
          tags.save()
          tags.post.add(post)

class Tags(BaseModel):

  tags = models.CharField(max_length=20, unique=True, blank=True)
  post = models.ManyToManyField(Post)
  objects = TagsManager()

  def __str__(self):
    return self.tags

  def clean(self):
    print('cleaning')
    self.tags = self.tags.strip('', '#')

