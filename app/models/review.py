from django.db.models import *


class Review(Model):
    class Meta:
        verbose_name = "Отзыв покупателя"
        verbose_name_plural = "Отзывы покупателей"

    def __str__(self):
        return f"{self.title} / {self.date}"

    title = CharField(verbose_name='Заголовок', max_length=1023)
    author = CharField(verbose_name='Автор', max_length=1023)
    url = URLField('Ссылка')
    date = DateField('Дата')
    pros = TextField('Плюсы')
    cons = TextField('Минусы')
