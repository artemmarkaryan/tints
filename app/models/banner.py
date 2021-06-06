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
import helpers
from django.core.management import call_command


class Banner(ModelWithImage):
    title = CharField(max_length=1023, verbose_name='Заголовок')
    text = TextField('Текст')
    buttonText = CharField(max_length=128, verbose_name='Текст кнопки')
    buttonUrl = URLField(verbose_name='Ссылка кнопки')
    background_lg = FileField(
        'Файл фона баннера (Десктоп)', null=True, blank=True)
    background_lg_url = URLField(
        'Ссылка на фон баннера (Десктоп)', null=True, blank=True)
    background_sm = FileField(
        'Файл фона баннера (Телефон)', null=True, blank=True)
    background_sm_url = URLField(
        'Ссылка на фон баннера (Телефон)', null=True, blank=True)

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"

    def __str__(self):
        return self.title

    def save(self, *a, **kw):
        url = self.background_lg_url
        if url:
            self.background = helpers.images.download_image_from_source(url)
            self.background_lg_url = None

        url = self.background_sm_url
        if url:
            self.background_sm = helpers.images.download_image_from_source(url)
            self.background_sm_url = None

        call_command('collectstatic', verbosity=0, interactive=False)
        super().save()
