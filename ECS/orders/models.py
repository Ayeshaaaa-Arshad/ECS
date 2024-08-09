from django.db import models
from users.models import User
from products.models import Product

# Add to Cart model
class AddToCart(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'Customer'})
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()  # Ensures quantity is positive

    def __str__(self):
        return f'Cart Item {self.id} - Customer {self.customer.username}'

# Orders model
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'Customer'})
    order_date = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return f'Order {self.order_id} by {self.customer.username}'

#Order Item Model to make sure the items in order is from Add to Cart model
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    cart_item = models.ForeignKey(AddToCart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'Order Item {self.id} for Order {self.order.order_id}'
