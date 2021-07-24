from django.db.models import *


class SkuVideo(Model):
    sku = ForeignKey('Sku', verbose_name='SKU', on_delete=CASCADE)
    url = TextField('Ссылка на видео')