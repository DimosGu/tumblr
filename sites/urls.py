from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^mini_site$', views.mini_site, name='mini_site'),
	url(r'^get_ten_posts$', views.get_ten_posts, name='get_ten_posts'),
]