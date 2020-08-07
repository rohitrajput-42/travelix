from django.urls import path
from . import views

urlpatterns = [
    path('gallery', views.gallery, name = 'gallery'),
    path('hom', views.hom, name = 'hom'),
] 
 