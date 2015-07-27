from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^', include('no_user.urls')),
	url(r'^dashboard/', include('dashboard.urls')),
	# url(r'^posts/', include('posts.urls')),
	url(r'^user_accounts/', include('user_accounts.urls')),
	url(r'^admin/', include(admin.site.urls)),
]
