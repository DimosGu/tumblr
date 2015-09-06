from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^logout$', views.log_out, name='log_out'),
]