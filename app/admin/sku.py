from django.contrib import admin
from ..models import Sku, SkuImage


class SkuImageAdminInline(admin.TabularInline):
    model = SkuImage


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
    inlines = [SkuImageAdminInline]
