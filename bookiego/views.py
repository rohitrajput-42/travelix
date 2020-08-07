from django.shortcuts import render
from .models import Book

def bookinggoa(request):
    if request.method == 'POST': 
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        package_name = request.POST.get('package_name', '')

        book = Book(first_name = first_name, last_name = last_name, phone = phone, email = email, address = address, package_name = package_name)
        book.save()
        return render(request, 'bookinggoa.html')
    else:
        return render(request, "bookinggoa.html")