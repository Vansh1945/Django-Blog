from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL
    path('', include('blog_app.urls')),  # Include URLs from blog_app
    path('tinymce/', include('tinymce.urls')),  # URL for TinyMCE
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serve media files during development

urlpatterns += staticfiles_urlpatterns()  # Serve static files during development
