from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', lambda request: redirect('participants/')),  # Redirige la raíz a /participants/
    path('admin/', admin.site.urls),
    path('participants/', include('participants.urls')),
    path('roulette/', include('roulette.urls')),
    path('login/', include('Login.urls')),
    path('registro/', include('registro.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)