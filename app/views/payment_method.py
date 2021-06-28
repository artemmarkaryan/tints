from helpers import wrap_response
from app.services import payment_method


def get_all(_):
    return wrap_response.wrap_data(payment_method.get_all())
