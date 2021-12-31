from django.conf import settings


def get_order_link(order):
    return f'{settings.HOST}/order?id={order.id}&key={order.hash}'
