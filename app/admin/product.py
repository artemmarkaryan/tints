from django.contrib import admin
from ..models import (
    Product,
    ProductInfo,
    Sku,
)


class SkuAdminInline(admin.TabularInline):
    model = Sku


class ProductInfoInline(admin.TabularInline):
    model = ProductInfo


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    filter_horizontal = ['related']
    fields = [
        "name",
        "category",
        "translit_name",
        "description",
        "new",
        "top",
        "bestseller",
        "related"
    ]
    readonly_fields = ['translit_name']
    inlines = [ProductInfoInline, SkuAdminInline]
