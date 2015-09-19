from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^post_photo$', views.post_photo, name='post_photo'),
	url(r'^post_text$', views.post_text, name='post_text'),
	url(r'^edit_post$', views.edit_post, name='edit_post'),
	url(r'^delete_post$', views.delete_post, name='delete_post'),
	url(r'^get_more_posts$', views.get_more_posts, name='get_more_posts'),
	url(r'^(?P<username>[\s\S]+)$', views.blog_edit, name='blog_edit'),
]