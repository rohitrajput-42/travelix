from django.urls import path
from . import views

urlpatterns = [
    path('goa', views.goa, name = 'goa'),
    path('hom', views.hom, name = 'hom')
] 
 