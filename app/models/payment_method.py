from django.db.models import *


class PaymentMethod(Model):
    class Meta:
        verbose_name = 'Способ оплаты'
        verbose_name_plural = 'Способы оплаты'

    def __str__(self):
        return f"{self.code} | {self.name}"

    id = AutoField(primary_key=True)
    code = CharField(verbose_name='Код', max_length=256)
    name = CharField(verbose_name='Название', max_length=256)
