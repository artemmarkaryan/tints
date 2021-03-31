from django.db.models import *
from .model_with_image import ModelWithImage


class SkuImage(ModelWithImage):
    sku = ForeignKey('Sku', verbose_name='SKU', on_delete=CASCADE)
