from django.db import models
from orders.models import Order

# Shipments model
class Shipment(models.Model):
    shipment_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    shipment_date = models.DateField()

    def __str__(self):
        return f'Shipment {self.shipment_id} for Order {self.order.order_id}'
