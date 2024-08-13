from django.db import models
from orders.models import Order

# Shipments model
class Shipment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f'Shipment {self.id}'
