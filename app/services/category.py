from django.db.models import F
from ..models import (
    Category,
)


def get_all():
    categories = list(
        Category.objects.annotate(
            translit=F('translit_name')
        ).values('id', 'name', 'translit')
    )
    return categories
