from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.settings, name='settings'),
  url(r'^blog/(?P<username>\w+)$', views.blog_appearance, name='blog_appearance'),
]