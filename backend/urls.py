
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.delivery.views import OrderViewSet

router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
