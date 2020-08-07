from django.urls import path
from . import views

urlpatterns = [
    path('auli', views.auli, name = 'auli'),
    path('hom', views.hom, name = 'hom')
] 
 