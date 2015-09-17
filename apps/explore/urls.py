from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.explore, name='explore'),
	url(r'^recent$', views.recent, name='recent'),
  url(r'^text$', views.text, name='text'),
  url(r'^photo$', views.photo, name='photo'),
	url(r'^get_ten_posts$', views.get_ten_posts, name='get_ten_posts'),
]