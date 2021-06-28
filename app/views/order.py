import json
from django.db import IntegrityError
from helpers import wrap_response
from app.services import order
from app.models import Order

def new(request):
    keys = (
        'name',
        'email',
        'phone',
        'paymentMethodCode',
        'shippingMethodId',
        'items'
    )
    body = json.loads(request.body)
    for key in keys:
        if body.get(key) is None:
            return wrap_response.wrap_error(
                f"Не передан параметр {key}",
            )

    try:
        new_order = order.new(body)
        return wrap_response.wrap_data(
            {
                "orderId": new_order.id,
                "key": new_order.hash,
            }
        )
    except Exception as e:
        return wrap_response.wrap_error(
            f"Не получиось создать заказ: {e}"
        )


def get(request, order_id):
    try:
        key = request.GET.get('key')
        return wrap_response.wrap_data(order.get(order_id, key))

    except Order.DoesNotExist as e:
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


def update_order_payment_status(request, order_id):
    # todo
    ...
