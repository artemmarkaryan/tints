from django.db.models import *
from .model_with_image import ModelWithImage


class SkuImage(ModelWithImage):
    sku = ForeignKey('Sku', verbose_name='SKU', on_delete=CASCADE)
    image = FileField(verbose_name='Файл изображения', null=True, blank=True)
    image_url = CharField(verbose_name='Ссылка яна изображение', max_length=1023)