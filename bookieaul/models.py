from django.db import models
from datetime import datetime, date

class Book(models.Model):
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=90)    
    phone = models.CharField(max_length = 100)
    email = models.TextField()
    address = models.TextField()
    amount = models.CharField(max_length = 100)
    booking_date = models.DateField()
    package_name = models.TextField()

    def __str__(self):
        return self.first_name

