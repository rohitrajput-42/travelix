from django.shortcuts import render, redirect

def agra(request):
    return render(request, 'agra.html') 

def hom(request):
    return redirect('/')
