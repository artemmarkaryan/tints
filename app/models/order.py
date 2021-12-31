import time
from django.db.models import *
import app.notifications.unione as unione
import app.notifications.sms as sms
import app.models.item as item
from helpers import random_hash, generate_tag, generate_link


class Order(Model):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"{self.id} {self.name} {self.phone} {self.created}"

    def save(self, *a, **kw):
        if self.pk is None:
            orig = None
            self.shipping_price = self.shipping_method.price
        else:
            orig = Order.objects.get(id=self.id)

        super().save(*a, **kw)
        new = Order.objects.get(id=self.id)
        OrderHandler(orig, new).handle()

    id = AutoField(primary_key=True)
    created = DateTimeField(verbose_name='Дата создания',
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
    payment_id = IntegerField(
        verbose_name='Id платежа в Тинькоф', null=True, blank=True
    )
    paid = BooleanField(verbose_name='Оплачен', default=False)

    # shipping
    shipping_method = ForeignKey('ShippingMethod',
                                 verbose_name='Способ доставки',
                                 on_delete=RESTRICT, null=True, blank=True)
    shipping_price = FloatField(verbose_name="Стоимость доставки", default=0)
    shipping_date = CharField(verbose_name='Дата доставки', max_length=48,
                              null=True, blank=True)
    shipping_time = CharField(verbose_name='Время доставки', max_length=32,
                              null=True, blank=True)

    @property  # стоимость всех продуктов
    def items_price(self) -> float:
        return sum([i.price * i.quantity for i in
                    item.Item.objects.filter(order=self)])

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
        unione.get_api().send_mail(
            to=self.new.email,
            subj=f"Заказ #{self.new.id} оформлен",
            text=f"Пожалуйста, дождитесь звонка, смс или email о "
                 f"подтверждении заказа. Детали и оплата:"
                 f" {generate_tag.get_order_tag(self.new)}"
        )

    def __changed(self):
        action = {
            "approved": self.__approved,
            "preparing": self.__preparing,
            "sent": self.__sent,
            "received": self.__received,
            "canceled": self.__canceled,
        }.get(self.new.status.code)

        if action is None:
            action = self.__change_unknown

        action()

    def __approved(self):
        if self.new.payment_method.code == "online":
            message = f"\nДетали и оплата: "
        else:
            message = f"\nДетали: "

        unione.get_api().send_mail(
            to=self.new.email,
            subj=f"Заказ #{self.new.id} подтверждён",
            text=f"Заказ подтверждён. Скоро его начнут собирать." +
                 message + f"{generate_tag.get_order_tag(self.new)}"

        )
        sms.send(
            self.new.phone,
            f"Заказ #{self.new.id} подтверждён. Скоро его начнут собирать." +
            message + f'{generate_link.get_order_link(self.new)}'
        )

    def __preparing(self):
        unione.get_api().send_mail(
            to=self.new.email,
            subj=f"Заказ #{self.new.id} уже собирают",
            text=f"Детали: {generate_tag.get_order_tag(self.new)}"
        )

    def __sent(self):
        unione.get_api().send_mail(
            to=self.new.email,
            subj=f"Заказ #{self.new.id} уже отправлен",
            text=f"Детали: {generate_tag.get_order_tag(self.new)}"
        )
        sms.send(
            self.new.phone,
            message=f'Заказ #{self.new.id} отправлен. Детали: '
                    f'{generate_link.get_order_link(self.new)}'
        )

    def __received(self):
        unione.get_api().send_mail(
            to=self.new.email,
            subj=f"Заказ #{self.new.id} доставлен",
            text=f"Детали: {generate_tag.get_order_tag(self.new)}"
        )
        sms.send(
            self.new.phone,
            message=f'Заказ #{self.new.id} доставлен. '
                    f'Спасибо, что выбрали Tintsofnature!'
        )

    def __canceled(self):
        unione.get_api().send_mail(
            to=self.new.email,
            subj=f"Заказ #{self.new.id} отменён",
            text=f"Детали: {generate_tag.get_order_tag(self.new)}"
        )
        sms.send(
            self.new.phone,
            message=f'Заказ #{self.new.id} отменён'
        )

    def __change_unknown(self):
        unione.get_api().send_mail(
            to=self.new.email,
            subj=f"Заказ #{self.new.id} изменён",
            text=f"Детали: {generate_tag.get_order_tag(self.new)}"
        )
