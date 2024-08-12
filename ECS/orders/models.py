from django.db import models
from users.models import Customer
from products.models import Product
from shops.models import Shop


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)


class AddToCart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    cart_item = models.ForeignKey(AddToCart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
