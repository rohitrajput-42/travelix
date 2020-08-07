from django.urls import path
from . import views

urlpatterns = [
    path('bookingauli', views.bookingauli, name = 'bookingauli')
]