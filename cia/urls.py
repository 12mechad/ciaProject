from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.defaults import server_error

from cia.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Dashboard.urls')),
    path('accounts/', include('accounts.urls')),
    path('immobilier/', include('immobilier.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
if settings.DEBUG:
    urlpatterns += static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static (settings.STATIC_URL,document_root=settings.STATIC_ROOT)