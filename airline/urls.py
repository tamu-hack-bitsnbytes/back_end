from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_flights/', views.get_flights, name='get_flights'),
    path('get_donations/', views.get_donations, name='get_donations'),
]