from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.dashboard, name='dashboard'),
	url(r'^get_ten_posts$', views.get_ten_posts, name='get_ten_posts'),
]