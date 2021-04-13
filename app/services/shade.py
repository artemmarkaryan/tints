from django.db.models import F
from ..models import (
    Shade
)


def get_all():
    return list(
        Shade.objects.all().annotate().values('id', 'image')
    )