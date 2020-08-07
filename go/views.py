from django.shortcuts import render, redirect

def goa(request):
    return render(request, 'goa.html') 

def hom(request):
    return redirect('/')