from django.db.models import *
from .model_with_image import ModelWithImage
import helpers


class Shade(ModelWithImage):
    class Meta:
        verbose_name = 'Оттенок'
        verbose_name_plural = 'Оттенки'

    def __str__(self):
        return self.name

    name = CharField(verbose_name='Название', max_length=512)
