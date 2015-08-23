from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^', include('no_user.urls')),
	url(r'^sites', include('sites.urls')),
	url(r'^blog/', include('blog.urls')),
	url(r'^explore/', include('explore.urls', namespace="explore")),
	url(r'^user_accounts/', include('user_accounts.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^dashboard/', include('dashboard.urls', namespace='dashboard')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)	