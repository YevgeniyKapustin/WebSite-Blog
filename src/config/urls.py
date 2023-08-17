from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config import settings

urlpatterns: list[path] = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('articles/', include('articles.urls')),
]

if settings.DEBUG:
    import socket
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = (
            [ip[: ip.rfind(".")] + ".1" for ip in ips] +
            ["127.0.0.1", "10.0.2.2"]
    )
