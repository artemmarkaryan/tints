from django.db.models import *


class Sku(Model):
    product = ForeignKey('Product', on_delete=RESTRICT)
    name = CharField(verbose_name='Название', max_length=512)
    translitName = CharField(verbose_name='Транслит', max_length=512, null=True, blank=True)
    vendorCode = CharField(verbose_name='Название', max_length=512, unique=True)
    oldPrice = FloatField(verbose_name='Старая цена', null=True, blank=True)
    price = FloatField(verbose_name='Цена')
    weight = IntegerField(verbose_name='Объём (мл)')