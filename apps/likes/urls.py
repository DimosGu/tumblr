from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.likes, name='likes'),
  url(r'^like$', views.like, name='like'),
  url(r'^unlike$', views.unlike, name='unlike'),
]