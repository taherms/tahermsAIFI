from django.db import models

# Create your models here.
class Product(models.Model):
    productname = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discription = models.TextField()
    gender = models.CharField(max_length=10)
    category = models.CharField(max_length=15)
    bestSellers = models.BooleanField(default=False)
    image = models.CharField(max_length=5000, null=True, blank=True)

