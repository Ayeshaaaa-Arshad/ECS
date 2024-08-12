from django.db import models
from django.apps import apps

class ProductCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    shop = models.ForeignKey('shops.Shop', on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Product {self.id}'
    
    def get_related_shop(self):
        Shop = apps.get_model('shops', 'Shop')
        return Shop.objects.get(id=self.shop_id)
