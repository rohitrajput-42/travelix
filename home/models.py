from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length = 100)             
    img = models.ImageField(upload_to = 'pics')
    hname = models.TextField()
    pname = models.TextField()
    desc = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Testimonials(models.Model):
    desc = models.TextField()
    name = models.CharField(max_length = 1000)
    
    def __str__(self):
        return self.name

class Hotels(models.Model):
    img = models.ImageField(upload_to = 'hotels')
    name = models.CharField(max_length = 150)
    viwe = models.IntegerField()
    point = models.TextField()
    price = models.IntegerField()
    desc = models.TextField()

    def __str__(self):
        return self.name