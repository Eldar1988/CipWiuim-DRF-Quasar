from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path('blog/', include('blog.urls')),
    path('forum/', include('forum.urls')),
    path('contacts/', include('contacts.urls')),
    path('map/', include('map_points.urls')),
    path('', include('cipwiuim.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
