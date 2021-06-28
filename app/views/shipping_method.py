from helpers import wrap_response
from app.services import shipping_method


def get_all(_):
    return wrap_response.wrap_data(shipping_method.get_all())
