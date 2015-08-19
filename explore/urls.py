from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.explore, name='explore'),
	url(r'^trending$', views.trending, name='trending'),
]