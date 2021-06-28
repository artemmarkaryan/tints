from app.models import ShippingMethod


def get_all():
    return list(ShippingMethod.objects.all().values(
        'id', 'name', 'description', 'price'))