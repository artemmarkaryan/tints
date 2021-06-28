from django.db.models import *


class Item(Model):
    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def __str__(self):
        return f"{self.sku.vendor_code} | {self.quantity} шт"

    id = AutoField(primary_key=True)
    order = ForeignKey('Order', verbose_name='Заказ', on_delete=CASCADE)
    sku = ForeignKey('Sku', verbose_name='Sku', on_delete=RESTRICT)
    price = FloatField(verbose_name='Цена при заказе')
    quantity = PositiveIntegerField(verbose_name='Количество')
