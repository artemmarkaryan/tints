from django.db.models import *


class ShippingMethod(Model):
    class Meta:
        verbose_name = 'Способ доставки'
        verbose_name_plural = 'Способы доставки'

    def __str__(self):
        return self.name

    id = AutoField(primary_key=True)
    name = CharField(max_length=255, verbose_name='Название')
    description = CharField(verbose_name='Описание', max_length=511, null=True,
                            blank=True)
    price = FloatField(verbose_name='Цена')
