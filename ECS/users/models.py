from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User model inheriting from AbstractUser
class User(AbstractUser):
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class Customer(models.Model):
    user = models.OneToOneField(User,related_name='customer_profile',on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Customer'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class AppAdmin(models.Model):
    user = models.OneToOneField(User,related_name='app_admin_profile',on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'AppAdmin'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
class ShopAdmin(models.Model):
    user = models.OneToOneField(User,related_name='shop_admin_profile',on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'ShopAdmin'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
