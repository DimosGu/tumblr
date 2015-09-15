from django.conf.urls import url
from . import views


urlpatterns = [
  url(r'^$', views.following, name='following'),
  url(r'^unfollow$', views.unfollow, name='unfollow'),
  url(r'^follow$', views.follow, name='follow'),
]