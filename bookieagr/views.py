from django.shortcuts import render, redirect
from .models import Book

def bookingagra(request):
    if request.method == 'POST': 
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        amount = request.POST.get('amount', '')
        booking_date = request.POST.get('booking_date', '')
        package_name = request.POST.get('package_name', '')

        book = Book(first_name = first_name, last_name = last_name, phone = phone, email = email, address = address, amount = amount,  booking_date = booking_date, package_name = package_name)
        book.save()
        return render(request, 'confirm.html')
    else:
        return render(request, "bookingagra.html")

