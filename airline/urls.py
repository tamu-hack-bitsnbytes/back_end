from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.index, name='index'),
    url('get_flights/', views.get_flights, name='get_flights'),
    url('get_donations/', views.get_donations, name='get_donations'),
]