from django.db import models

class Gallery(models.Model):
    img = models.ImageField(upload_to = 'gallery')
    name = models.CharField(max_length = 150)
    pkg = models.TextField()
    pname = models.TextField()

    def __str__(self):
        return self.name