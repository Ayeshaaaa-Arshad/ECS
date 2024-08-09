from django.db import models

# Product Category model
class ProductCategory(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.product_name


# Product model
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    description = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return f'Product {self.id} in Category {self.product_category.product_name}'
