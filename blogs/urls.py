from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^post_text$', views.post_text, name='post_text'),
	url(r'^post_photo$', views.post_photo, name='post_photo'),
	url(r'^delete_post$', views.delete_post, name='delete_post'),
	url(r'^(?P<username>\w+)$', views.blog_edit, name='blog_edit'),
]