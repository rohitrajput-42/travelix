from django.shortcuts import render, redirect

def places(request):
    return render(request, 'places.html') 

def hom(request):
    return redirect('/')