import json
from django.db import IntegrityError
import django.http
from helpers import wrap_response
from app import (
    services,
    models
)


def create(request):
    keys = (
        'name',
        'email',
        'phone',
        'paymentMethodCode',
        'shippingMethodId',
        'items'
    )
    body: dict = json.loads(request.body)
    for key in keys:
        if body.get(key) is None:
            return wrap_response.wrap_error(
                f"Не передан параметр {key}",
            )

    try:
        new_order = services.order.new(body)
        return wrap_response.wrap_data(
            {
                "orderId": new_order.id,
                "key": new_order.hash,
            }
        )
    except Exception as e:
        return wrap_response.wrap_error(
            f"Не получиось создать заказ: {e}, {e.__traceback__}"
        )


def get(request, order_id):
    try:
        key = request.GET.get('key')
        return wrap_response.wrap_data(services.order.get(order_id, key))

    except models.Order.DoesNotExist as e:
        return wrap_response.wrap_error(
            f"Не найден заказ #{order_id}",
            404
        )

    except IntegrityError:
        return wrap_response.wrap_error(
            f"Неверный ключ",
            403
        )

    except Exception as e:
        return wrap_response.wrap_error(
            f"Не найти заказ: {e}"
        )


def pay(request, order_id):
    try:
        key = request.GET.get('key')
        if key is None:
            return wrap_response.wrap_error('Не передан ключ')
        return wrap_response.wrap_data(
            {'paymentUrl': services.order.initialize_payment(order_id)}
        )

    except models.Order.DoesNotExist:
        return wrap_response.wrap_error('Заказа не существует', 404)


def payment_notification(request):
    response = json.loads(request.body)
    if response['Status'] == "CONFIRMED":
        try:
            services.order.update_order_payment_status(
                order_id=response['OrderId'],
                payment_id=response['PaymentId'],
            )
        except models.Order.DoesNotExist:
            # todo: handle
            pass
    return django.http.HttpResponse("OK")
