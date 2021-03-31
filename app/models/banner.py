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
    title = CharField(1023, verbose_name='Заголовок')
    text = TextField('Текст')
    buttonText = CharField(128, verbose_name='Текст кнопки')
    buttonUrl = URLField(verbose_name='Ссылка кнопки')
