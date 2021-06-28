from django.db.models import *


class OrderStatus(Model):
    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'

    def __str__(self):
        return self.verbose_name

    id = AutoField(primary_key=True)
    code = CharField(verbose_name='Код', max_length=128)
    verbose_name = CharField(verbose_name='Название', max_length=256)
