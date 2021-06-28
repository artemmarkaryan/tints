from django.db.models import F
from django.db import transaction
from django.db import *
import copy
from app.models import (
    Order,
    Item,
    Sku,
    PaymentMethod,
    ShippingMethod,
    OrderStatus,
)


@transaction.atomic
def new(body) -> Order:
    payment_method = PaymentMethod.objects.get(
        code=body.get('paymentMethodCode')
    )
    shipping_method = ShippingMethod.objects.get(
        id=body.get('shippingMethodId')
    )

    order = Order.objects.create(
        name=body['name'],
        phone=body['phone'],
        email=body['email'],
        comment=body.get('comment'),
        payment_method=payment_method,
        shipping_method=shipping_method,
        paid=False,
        status=OrderStatus.objects.get(code='initial')
    )

    for item in body['items']:
        Item.objects.create(
            order=order,
            sku_id=item['skuId'],
            quantity=item['quantity'],
            price=Sku.objects.get(id=item['skuId']).price
        )

    return order


def get(order_id, key):
    order_query = Order.objects.filter(id=order_id)
    if len(order_query) == 0:
        raise Order.DoesNotExist
    if order_query[0].hash != key:
        raise IntegrityError

    order_dict = copy.deepcopy(order_query).annotate(
        shippingDate=F('shipping_date'),
        shippingTime=F('shipping_time'),
    ).values(
        'name',
        'email',
        'phone',
        'address',
        'comment',
        'shippingDate',
        'shippingTime',
    )
    order_dict = order_dict[0]
    order_instance = order_query[0]
    order_dict['shippingPrice'] = order_instance.shipping_price
    order_dict['itemsPrice'] = order_instance.items_price
    order_dict['fullPrice'] = order_instance.full_price
    order_dict['status'] = order_instance.status.verbose_name
    order_dict['canPay'] = order_instance.status.code == 'approved'

    order_dict['items'] = list(Item.objects.filter(
        order_id=order_instance.id
    ).annotate(
        skuId=F('sku_id'),
        name=F('sku__product__name'),
    ).values(
        'skuId',
        'name',
        'quantity',
        'price'
    ))

    return order_dict


def update_order_payment_status():
    # todo
    ...


def validate():
    # todo
    ...
