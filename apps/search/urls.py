from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.search, name='search'),
  url(r'^get_ten_posts$', views.get_ten_posts, name='get_ten_posts'),
  url(r'^(?P<results>[\s\S]+)$', views.results, name='results'),
]