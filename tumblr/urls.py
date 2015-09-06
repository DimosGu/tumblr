from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^', include('apps.no_user.urls')),
  url(r'^search/', include('apps.search.urls')),
	url(r'^sites/', include('apps.sites.urls')),
	url(r'^blog/', include('apps.blog.urls')),
	url(r'^explore/', include('apps.explore.urls', namespace="explore")),
	url(r'^user_accounts/', include('apps.user_accounts.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^dashboard/', include('apps.dashboard.urls', namespace='dashboard')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)