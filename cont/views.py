from django.shortcuts import render, redirect

def contact(request):
    return render(request, 'contact.html') 

def hom(request):
    return redirect ('/')