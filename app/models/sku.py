from django.db.models import *


class Sku(Model):
    class Meta:
        verbose_name = "SKU"
        verbose_name_plural = "SKU"

    def __str__(self):
        return f"{self.product.name}"

    product = ForeignKey('Product', on_delete=RESTRICT, verbose_name='Продукт')
    vendor_code = CharField(verbose_name='Артикул', max_length=512, unique=True)
    old_price = FloatField(verbose_name='Старая цена', null=True, blank=True)
    price = FloatField(verbose_name='Цена')
    shade = ForeignKey('Shade', verbose_name='Оттенок', null=True, blank=True, on_delete=RESTRICT)
    weight = IntegerField(verbose_name='Объём (мл)', null=True, blank=True)
