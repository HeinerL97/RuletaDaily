from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('delete/<int:pk>/', views.delete_participant, name='delete_participant'),
]