
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('vendor', 'Vendor'),
        ('driver', 'Driver'),
        ('admin', 'Admin'),
    )
    phone = models.CharField(max_length=15, unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username']
