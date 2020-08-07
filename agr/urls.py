from django.urls import path
from . import views

urlpatterns = [
    path('agra', views.agra, name = 'agra'),
    path('hom', views.hom, name = 'hom')
] 
 