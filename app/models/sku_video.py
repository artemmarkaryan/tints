from django.db.models import *


class SkuVideo(Model):
    sku = ForeignKey('Sku', verbose_name='SKU', on_delete=CASCADE)
    url = CharField('Ссылка на видео', max_length=1024)