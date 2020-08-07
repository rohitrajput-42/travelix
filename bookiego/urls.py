from django.urls import path
from . import views

urlpatterns = [
    path('bookinggoa', views.bookinggoa, name = 'bookinggoa')
]