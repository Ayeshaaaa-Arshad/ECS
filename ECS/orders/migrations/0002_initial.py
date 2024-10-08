# Generated by Django 5.1 on 2024-08-09 13:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
        ('products', '0002_initial'),
        ('shops', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtocart',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customer'),
        ),
        migrations.AddField(
            model_name='addtocart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.shop'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='cart_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.addtocart'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order'),
        ),
    ]
