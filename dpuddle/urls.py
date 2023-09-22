from django.contrib import admin
from django.urls import path
from core.views import index, contact
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('about/', index, name='about'),
]# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
#     urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
