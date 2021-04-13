from django.db.models import *


class Category(Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    name = CharField(verbose_name='Название', max_length=255)
    translit_name = CharField(verbose_name='Транслит', max_length=255)