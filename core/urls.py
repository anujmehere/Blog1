from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls', namespace='accounts')),
    path('account/', include('django.contrib.auth.urls')),
    path('', include('blog.urls', namespace='blog')),
    path('services/', include('services.urls', namespace='services')),
] 
if settings.DEBUG: #mapping static and media url when debug is enabled
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Future Today"
admin.site.site_title = "Future Today Admin Portal"
admin.site.index_title = "Welcome to Future Today Solutions"
