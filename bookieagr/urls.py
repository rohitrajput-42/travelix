from django.urls import path
from . import views

urlpatterns = [
    path('bookingagra', views.bookingagra, name = 'bookingagra'),
]