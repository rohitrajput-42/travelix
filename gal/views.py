from django.shortcuts import render, redirect
from .models import Gallery

def gallery(request):

    gallerys = Gallery.objects.all()

    return render(request, 'gallery.html', {"gallerys" : gallerys})

def hom(request):
    return redirect('/')