from django.shortcuts import render, redirect

def auli(request):
    return render(request, 'auli.html') 

def hom(request):
    return redirect('/')