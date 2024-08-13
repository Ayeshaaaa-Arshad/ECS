from django.db import models
from products.models import Product


class Shop(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)


class Stock(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
