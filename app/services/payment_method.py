from app.models import PaymentMethod


def get_all():
    return list(PaymentMethod.objects.all().values('code', 'name'))