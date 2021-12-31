from helpers import generate_link


def get_order_tag(order):
    return f'<a href="{generate_link.get_order_link(order)}">' \
           f'Заказ #{order.id}' \
           f'</a><br>'
