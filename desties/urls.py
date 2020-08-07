from django.urls import path
from . import views

urlpatterns = [
    path('places', views.places, name = 'places'),
    path('hom', views.hom, name = 'hom')
] 
 