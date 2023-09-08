from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from places import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_map),
    path('places/<int:location_id>/', views.show_location_properties,
         name='places'),
    path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
