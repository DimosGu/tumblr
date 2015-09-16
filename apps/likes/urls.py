from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.likes, name='likes'),
  url(r'^like$', views.like, name='like'),
  url(r'^unlike$', views.unlike, name='unlike'),
  url(r'^ten_more_posts$', views.ten_more_posts, name='ten_more_posts'),
]