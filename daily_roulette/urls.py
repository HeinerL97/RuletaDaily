from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', lambda request: redirect('login/')),  # Redirige la raíz a /participants/
    path('admin/', admin.site.urls),
    path('participants/', include('participants.urls')),
    path('proyecto/', include('proyecto.urls')),
    path('login/', include('Login.urls')),  # o views.login_view si no usas include
    path('registro/', include('registro.urls')),
    path('', include('participants.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)