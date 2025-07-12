from django.urls import path
from . import views
app_name = 'proyecto'

urlpatterns = [
    path('', views.proyectos_list, name='proyectos'),
    path('eliminar/<int:proyecto_id>/', views.eliminar_proyecto, name='eliminar_proyecto'),
]