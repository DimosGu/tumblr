from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.search, name='search'),
  url(r'^(?P<results>[\s\S+]+)$', views.results, name='results'),
  url(r'^get_ten_posts/(?P<results>[\s\S+]+)$', views.get_ten_posts, name='get_ten_posts'),
]