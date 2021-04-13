from django.db.models import F
from ..models import (
    Banner,
)


def get_all():
    return list(
        Banner.objects.values('title', 'text', 'buttonText', 'buttonUrl', 'image')
    )

