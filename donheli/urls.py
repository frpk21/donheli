from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path('', include(('generales.urls', 'generales'), namespace='generales')),
    path('', include(('generales.urls', 'generales'), namespace='base')),
    path('admin/', admin.site.urls),
]

urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)