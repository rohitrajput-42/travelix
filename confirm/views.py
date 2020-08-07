from django.shortcuts import render, redirect

def confrm(request):
    return render(request, 'confirm.html')
