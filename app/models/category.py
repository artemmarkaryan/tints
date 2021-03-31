from django.db.models import *


class Category(Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = CharField(verbose_name='Название', max_length=255)
    translitName = CharField(verbose_name='Транслит', max_length=255)