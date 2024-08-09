from django.contrib.auth.models import AbstractUser
from django.db import models
from users.constants import ROLES

# Custom User model inheriting from AbstractUser
class User(AbstractUser):
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=10, choices=ROLES, default='Customer')

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.role})'
    

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
