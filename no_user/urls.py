from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.register, name='register'),
	url(r'^register$', views.register, name='register'),
	url(r'^check_fields$', views.check_fields, name='check_fields'),
	url(r'^login$', views.user_login, name='login'),
]