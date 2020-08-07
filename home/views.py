from django.shortcuts import render, redirect
from .models import Destination, Testimonials, Hotels

def index(request):
    dests = Destination.objects.all()

    tests = Testimonials.objects.all()

    hotels = Hotels.objects.all()

    return render(request, 'index.html', {'dests' : dests, 'tests' : tests, 'hotels' : hotels} )

def hom(request):
    return redirect('/')