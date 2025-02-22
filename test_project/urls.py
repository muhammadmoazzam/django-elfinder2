from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from django.views.static import serve

admin.autodiscover()

urlpatterns = [
   path('elfinder/', include('elfinder.urls')),
   path('admin/', admin.site.urls),
]

if settings.DEBUG:
   urlpatterns += [
       path(f'{settings.MEDIA_URL[1:]}/<path:path>', serve, {
           'document_root': settings.MEDIA_ROOT,
       }),
   ]