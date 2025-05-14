
from django.db import models
from apps.authentication.models import User

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'قيد المعالجة'),
        ('in_transit', 'في الطريق'),
        ('delivered', 'تم التسليم'),
        ('cancelled', 'ملغي'),
    )

    package_id = models.CharField(max_length=20, unique=True)
    customer_name = models.CharField(max_length=100)
    address = models.TextField()
    contents = models.TextField(blank=True, null=True)
    delivery_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    vendor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders_sent')
    delivery_company = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders_received')
    driver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders_driven')
    created_at = models.DateTimeField(auto_now_add=True)
