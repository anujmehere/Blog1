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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
