from django.db.models import F
from django.db import transaction
from django.db import (
    Error as DbError,
    IntegrityError
)
from django.conf import settings
import copy
import requests

from helpers import wrap_response
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
        paymentMethod=F('payment_method'),
    ).values(
        'name',
        'email',
        'phone',
        'address',
        'comment',
        'shippingDate',
        'shippingTime',
        'paymentMethod'
    )
    order_dict = order_dict[0]
    order_instance = order_query[0]
    order_dict['paymentMethod'] = PaymentMethod.objects.get(
        id=order_dict['paymentMethod']).code
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


def update_order_payment_status(order_id, payment_id):
    try:
        order_instance = Order.objects.get(id=order_id)
        order_instance.paid = True
        order_instance.payment_id = payment_id
        order_instance.save()
        return True
    except DbError:
        return False


def pay(request, order_id):
    try:
        key = request.GET.get('key')
        if key is None:
            return wrap_response.wrap_error('Не передан ключ')
        return wrap_response.wrap_data(
            {'paymentUrl': initialize_payment(order_id)}
        )

    except Order.DoesNotExist:
        return wrap_response.wrap_error('Заказа не существует', 404)


def initialize_payment(order_id):
    order: Order = Order.objects.get(id=order_id)
    payload = {
        'TerminalKey': settings.PAYMENT_TERMINAL_ID,
        'Amount': 100 * order.full_price,
        'OrderId': str(order_id),
    }
    resp = requests.post(
        url=settings.INIT_PAYMENT_URL,
        json=payload
    )

    resp = resp.json()
    try:
        pay_form_url = resp['PaymentURL']
        return pay_form_url
    except KeyError:
        return payload, resp
