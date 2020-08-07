from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('hom', views.hom, name = 'hom')
]
