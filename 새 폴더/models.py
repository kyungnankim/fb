# myapp/models.py
from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images/')


'''
class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.title
'''