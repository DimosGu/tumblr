from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.site_or_register, name='site_or_register'),
	url(r'^register$', views.site_or_register, name='register'),
	url(r'^check_fields$', views.check_fields, name='check_fields'),
	url(r'^login$', views.user_login, name='login'),
]