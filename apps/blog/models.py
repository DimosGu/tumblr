from django.db import models
from django.conf import settings
from django.utils import timezone
from django.template.loader import render_to_string
from tumblr.base_model import BaseManager, BaseModel
from apps.user_accounts.models import User
from random import randint


def upload_path(self, filename):
  random_number = randint(0, 10000000000000000)
  file_extension = filename.split('.')[1]

  return 'user_media/%s/tumblr_%s.%s' % (self.user.username, random_number, file_extension)


class BlogManager(BaseManager):

  def get_blog_user(self, user):
    return self.get(user=user)

  def get_blog_pk(self, pk):
    return self.get(pk=pk)


class PostManager(BaseManager):

  def get_pk(self, pk):
    return self.get(pk=pk)

  def filter_blog(self, blog):
    return self.filter(blog=blog)

  def convert_liked_to_post(self, liked_posts):
    converted_posts = []

    for post in liked_posts:
      converted_posts.append(post.post)

    return converted_posts

  def combine_post_attributes(self, latest_posts, user=False, follow=False, like=False):
    from apps.following.models import Follow
    from apps.likes.models import Like
    from apps.search.models import Tags

    context = {
      'latest_posts': []
    }

    for post in latest_posts:
      tags_filter = Tags.objects.filter(post=post)
      tags = []

      for tag in tags_filter:
        tags.append(tag.tags)

      if like:

        try:
          like = Like.objects.get(user=user, post=post)
          like = 'True'
        except:
          like = 'False'

        if follow:
          blog = Blog.objects.get(user=post.user)

          try:
            following = Follow.objects.get(user=user, blog=blog)
            follow = 'True'
          except:
            follow = 'False'

          context['latest_posts'].append((post, tags, like, follow))
        else:
          context['latest_posts'].append((post, tags, like))

      else:
        context['latest_posts'].append((post, tags))

    return context

  def ten_more_posts(self, post_count, user=False, ajax_user=False, blog=False, explore=False, search=False):
    end_count = post_count + 10

    if ajax_user:
      get_user = User.objects.get(username=ajax_user)
    elif user:
      get_user = user
    else:
      get_user = False

    if explore:

      if explore == 'text':
        return self.exclude(user=user).filter(file='').order_by('-pub_date')[post_count:end_count]
      elif explore == 'photo':
        return self.exclude(user=user).exclude(file='').order_by('-pub_date')[post_count:end_count]
      else:
        return self.exclude(user=user).order_by('-pub_date')[post_count:end_count]

    elif search:

      if not user:
        return search.post.all()[post_count:end_count]
      else:
        return search.post.exclude(user=user)[post_count:end_count]

    else:
      blog = Blog.objects.get(user=get_user)
      return self.filter(blog=blog).order_by('-pub_date')[post_count:end_count]

  def render_posts(self, ordered_posts, template, user=False, section=False, domain=False):
    from apps.following.models import Follow
    from apps.likes.models import Like
    from apps.search.models import Tags

    post_html = []

    if section == 'explore':

      for post in ordered_posts:
        blog = Blog.objects.get(user=post.user)
        tags = Tags.objects.filter(post=post)

        try:
          follow = Follow.objects.get(user=user, blog=blog)
          follow = 'True'
        except:
          follow = 'False'

        try:
          like = Like.objects.get(user=user, post=post)
          like = 'True'
        except:
          like = 'False'

        post_html.append(render_to_string(
          template,
          {
            'user': user,
            'domain_url': domain,
            'section': 'explore',
            'post': post,
            'follow': follow,
            'tags': tags,
            'like': like,
          }
        ))

    elif section == 'mini':

      for post in ordered_posts:
        tags = Tags.objects.filter(post=post)

        try:
          like = Like.objects.get(user=user, post=post)
          like = "True"
        except:
          like = "False"

        post_html.append(render_to_string(
          template,
          {
            'post': post,
            'tags': tags,
            'mini_section': 'True',
            'like': like,
          }
        ))
    elif section == 'blog_edit':

      for post in ordered_posts:
        tags = Tags.objects.filter(post=post)

        post_html.append(render_to_string(
          template,
          {
            'post': post,
            'tags': tags,
            'section': 'blog',
          }
        ))
    elif section == 'likes':

      for post in ordered_posts:
        blog = Blog.objects.get(user=post.user)
        tags = Tags.objects.filter(post=post)

        try:
          follow = Follow.objects.get(user=user, blog=blog)
          follow = 'True'
        except:
          follow = 'False'

        try:
          like = Like.objects.get(user=user, post=post)
          like = 'True'
        except:
          like = 'False'

        post_html.append(render_to_string(
          template,
          {
            'post': post,
            'tags': tags,
            'like': like,
            'follow': follow,
            'section': 'likes',
          }
        ))
    else:

      for post in ordered_posts:
        tags = Tags.objects.filter(post=post)

        try:
          like = Like.objects.get(user=user, post=post)
          like = 'True'
        except:
          like = 'False'

        post_html.append(render_to_string(
          template,
          {
            'post': post,
            'tags': tags,
            'like': like,
          }
        ))

    return post_html

  def sort_following_posts(self, user, post_count):
    from apps.following.models import Follow

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

  def render_new_post(self, user, form):
    from apps.search.models import Tags

    if form.is_valid():
      form.instance.user = user
      form.instance.blog = Blog.objects.get(user=user)
      form_instance = form.save()

      post = form_instance

      new_tags = form.data['tags'].lower()
      Tags.objects.create_tags(new_tags, post)

      post_tags = []
      tags_filter = Tags.objects.filter(post=post)

      for tag in tags_filter:
        post_tags.append(tag.tags)

      response = {
        'html': [],
      }

      response['html'].append(render_to_string(
        'post.html',
        {
          'post': post,
          'user': user,
          'blog': form_instance.blog,
          'tags': post_tags,
          'section': 'blog',
        }
      ))

      return response


class Blog(BaseModel):

  user = models.ForeignKey(User)
  title = models.CharField(max_length=50, default="Untitled")
  img = models.ImageField(upload_to=upload_path, default='/media/default_blog_img.png')
  bg_img = models.ImageField(upload_to=upload_path, default='/media/default_blog_bg.png')
  objects = BlogManager()

  class Meta:
    app_label = 'blog'

  def __str__(self):
    return '%s-%s' % (self.user.username, self.title)


class Post(BaseModel):

  user = models.ForeignKey(User)
  blog = models.ForeignKey(Blog)
  title = models.TextField(blank=True)
  text = models.TextField(blank=True)
  file = models.FileField(upload_to=upload_path, blank=True)
  notes = models.IntegerField(default=0)
  objects = PostManager()

  class Meta:
    app_label = 'blog'

  def __str__(self):
    if self.title != "":
      return self.title
    elif self.file != "":
      return 'File'
    else:
      return 'Untitled'