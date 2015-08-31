from django.db import models
from django.conf import settings
from django.utils import timezone
from user_accounts.models import User
from tumblr.base_model import BaseManager, BaseModel
from django.template.loader import render_to_string


def upload_path(self, filename):
  return 'user_media/%s/%s' % (self.user.username, filename)


class BlogManager(BaseManager):

  def get_blog_user(self, user):
    return self.get(user=user)


class PostManager(BaseManager):

  def get_by_user_pk(self, user, pk):
    return self.get(user=user, pk=pk)

  def filter_blog(self, blog):
    return self.filter(blog=blog)

  def ten_more_posts(self, post_count, user=False, ajax_user=False, blog=False, return_fields=False, explore=False):
    end_count = post_count + 10

    if ajax_user:
      get_user = User.objects.get(username=ajax_user).pk
    elif user:
      get_user = user.pk
    else:
      get_user = False

    if not explore:
      blog = Blog.objects.get(pk=get_user)

    if return_fields:
      fields = {}
      fields['filtered_posts'] = self.filter(blog=blog).order_by('-pub_date')[post_count:end_count]
      fields['blog'] = blog

      return fields
    elif explore:
      return self.exclude(user=user).order_by('-pub_date')[post_count:end_count]
    else:
      return self.filter(blog=blog).order_by('-pub_date')[post_count:end_count]

  def loop_posts(self, ordered_posts, template, explore=False):

    post_html = []

    if explore:

      for post in ordered_posts:
        blog = Blog.objects.get(user=post.user)

        try:
          follow = Follow.objects.get(user=request.user, blog=blog)
          follow = 'true'
        except:
          follow = 'false'

        post_html.append(render_to_string(
          template,
          {
            'post': post,
            'following': follow,
          }
        ))

    else:

      for post in ordered_posts:
        post_html.append(render_to_string(
          template,
          {
            'post': post
          }
        ))

    return post_html

  def sort_following_posts(self, user, post_count):

    post_list = []
    end_count = post_count + 10
    following = Follow.objects.filter(user=user)

    for user_blog in following:
      user = User.objects.get(username=user_blog)
      blog = Blog.objects.get(user=user)
      posts = self.filter(blog=blog)

      for post in posts:
        post_list.append(post.id)

    latest_posts = Post.objects.filter(pk__in=post_list).order_by('-pub_date')[post_count:end_count]

    return latest_posts

class FollowManager(BaseManager):

  def follow_filter(self, user):
    return self.filter(user=user)

  def get_following(self, user, blog):
    return self.get(user=user, blog=blog)


class Blog(BaseModel):

  user = models.ForeignKey(User)
  title = models.CharField(max_length=50, default="Untitled")
  img = models.ImageField(upload_to=upload_path, default='/media/default_blog_img.png')
  bg_img = models.ImageField(upload_to=upload_path, default='/media/default_blog_bg.png')
  objects = BlogManager()

  def __str__(self):
    return self.user.username


class Post(BaseModel):

  user = models.ForeignKey(User)
  blog = models.ForeignKey(Blog)
  title = models.TextField(blank=True)
  text = models.TextField(blank=True)
  tags = models.TextField(blank=True)
  file = models.FileField(upload_to=upload_path, blank=True)
  objects = PostManager()

  def __str__(self):
    if self.title != "":
      return self.title
    elif self.file != "":
      return 'File'
    else:
      return 'Untitled'


class Follow(BaseModel):

  user = models.ForeignKey(User)
  blog = models.ForeignKey(Blog)
  objects = FollowManager()

  def __str__(self):
    return self.blog.user.username

