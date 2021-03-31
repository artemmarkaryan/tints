from django.db.models import *


class Product(Model):
    name = CharField(verbose_name='Название', max_length=511)
    translit_name = CharField(verbose_name='Транслит', max_length=511)
    description = TextField('Описание')
    shade = ForeignKey('Shade', verbose_name='Оттенок', null=True, blank=True, on_delete=RESTRICT)
    new = BooleanField(default=False)
    top = BooleanField(default=False)