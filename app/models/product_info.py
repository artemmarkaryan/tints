from django.db.models import *


class ProductInfo(Model):
    product = ForeignKey('Product', verbose_name='Продукт', on_delete=CASCADE)
    title = CharField('Заголовок', max_length=512)
    text = TextField('Текст')
