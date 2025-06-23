from django.urls import path
from . import views

urlpatterns = [
    path('', views.roulette_view, name='roulette'),
]