from django.contrib import admin
from django.urls import path , include
from core.views import index, contact, doctor
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('core.urls')),
    path('doctor/', doctor, name='doctor'),
    path('admin/', admin.site.urls),
    path('about/', index, name='about'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
