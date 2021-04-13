"""
Banner
- id: int
- title: string
- text: string
- image: string
- buttonText: string
- buttonUrl: string
"""

from django.db.models import *
from .model_with_image import ModelWithImage


class Banner(ModelWithImage):
    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"

    def __str__(self):
        return self.title

    title = CharField(max_length=1023, verbose_name='Заголовок')
    text = TextField('Текст')
    buttonText = CharField(max_length=128, verbose_name='Текст кнопки')
    buttonUrl = URLField(verbose_name='Ссылка кнопки')
