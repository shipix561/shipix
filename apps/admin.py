
from django.contrib import admin
from apps.delivery.models import Order
from apps.authentication.models import User

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('package_id', 'status', 'vendor', 'delivery_company', 'driver', 'delivery_date')

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('phone', 'username', 'role', 'is_active')
