from django.contrib import admin
from ..models import Sku, SkuImage, SkuVideo


class SkuImageAdminInline(admin.TabularInline):
    model = SkuImage


class SkuVideoAdminInline(admin.TabularInline):
    model = SkuVideo


@admin.register(Sku)
class SkuAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "id",
        "price",
        "vendor_code",
        "weight"
    ]
    list_editable = [
        "price"
    ]
    inlines = [SkuImageAdminInline, SkuVideoAdminInline]
