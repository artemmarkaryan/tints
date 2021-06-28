from django.db.models import *
from helpers import random_hash
import app.models.item as item


class Order(Model):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"{self.id} {self.name} {self.phone} {self.created}"

    def save(self, *a, **kw):
        if self.pk is None:
            orig = None
        else:
            orig = Order.objects.get(id=self.id)

        super().save(*a, **kw)
        new = Order.objects.get(id=self.id)
        OrderHandler(orig, new).handle()

    id = AutoField(primary_key=True)
    created = DateTimeField(verbose_name='Дата создания', auto_created=True,
                            null=True, blank=True)
    hash = CharField(verbose_name='Ключ', max_length=128,
                     default=random_hash.hash_string)
    name = CharField(verbose_name='Имя', max_length=128)
    phone = CharField(verbose_name='Телефон', max_length=128)
    email = CharField(verbose_name='Email', max_length=128)
    address = CharField(verbose_name='Адрес', max_length=512, null=True,
                        blank=True)
    comment = TextField(verbose_name='Комментарий', null=True, blank=True)
    status = ForeignKey('OrderStatus', verbose_name='Статус',
                        on_delete=RESTRICT, null=True)

    # payment
    payment_method = ForeignKey('PaymentMethod', verbose_name='Способ оплаты',
                                on_delete=RESTRICT, null=True)
    payment_id = IntegerField(verbose_name='Id платежа в Тинькоф', null=True)
    paid = BooleanField(verbose_name='Оплачен', default=False)

    # shipping
    shipping_method = ForeignKey('ShippingMethod', verbose_name='Способ доставки',
                                 on_delete=RESTRICT, null=True, blank=True)
    shipping_date = CharField(verbose_name='Дата доставки', max_length=48,
                              null=True, blank=True)
    shipping_time = CharField(verbose_name='Время доставки', max_length=32,
                              null=True, blank=True)

    @property  # стоимость всех продуктов
    def items_price(self) -> float:
        return sum([i.price * i.quantity for i in
                    item.Item.objects.filter(order=self)])

    @property  # стоимость доставки
    def shipping_price(self) -> float:
        return self.shipping_method.price

    @property  # полная стоимость
    def full_price(self) -> float:
        return self.shipping_price + self.items_price


class OrderHandler:
    def __init__(self, old: Order, new: Order):
        self.old = old
        self.new = new

    def handle(self):
        if self.old is None:
            if self.new is None:
                raise AttributeError
            else:
                self.__created()
        else:
            self.__changed()

    def __created(self):
        # todo
        ...

    def __changed(self):
        # todo
        ...
