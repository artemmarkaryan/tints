from django.db.models import *
from .model_with_image import ModelWithImage


class Article(ModelWithImage):
    # todo: убрать, если будем верстать
    title = CharField(verbose_name='Заголовок', max_length=1023)
    text = TextField('Текст')


class AdviseArticle(Article):
    pass


class AboutArticle(Article):
    pass

