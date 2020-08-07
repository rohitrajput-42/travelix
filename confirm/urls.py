from django.urls import path
from . import views

urlpatterns = [
    path('confrm', views.confrm, name = 'confrm'),
]   
