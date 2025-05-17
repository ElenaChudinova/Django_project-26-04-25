from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls', namespace='catalog')),
    path('', include('my_blog.urls', namespace='my_blog')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
