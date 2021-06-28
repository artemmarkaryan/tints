from django.contrib import admin
from ..models import (
    Order,
    OrderStatus,
    PaymentMethod,
    ShippingMethod
)


# class SkuAdminInline(admin.TabularInline):
#     model = Sku


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    pass


@admin.register(ShippingMethod)
class ShippingMethodAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    pass
