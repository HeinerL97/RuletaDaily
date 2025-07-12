# participants/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('participantes/<int:project_id>/', views.participantes_list, name='participantes_list'),
    path('participantes/<int:project_id>/guardar/', views.guardar_participantes, name='guardar_participantes'),
    path('participantes/delete/<int:pk>/', views.delete_participant, name='delete_participant'),
    path('participantes/agregar-temporal/', views.agregar_participante_temporal, name='agregar_participante_temporal'), 
]