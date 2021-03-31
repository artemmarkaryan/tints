from django.db.models import *


class Review(Model):
    title = CharField(verbose_name='Заголовок', max_length=1023)
    author = CharField(verbose_name='Автор', max_length=1023)
    url = URLField('Ссылка')
    date = DateField('Дата')
    pros = TextField('Плюсы')
    cons = TextField('Минусы')