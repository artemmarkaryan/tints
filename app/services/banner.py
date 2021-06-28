from django.db.models import F
from ..models import (
    Banner,
)


def get_all():
    return list(
        Banner.objects.annotate(
            backgroundLg=F('background_lg'),
            backgroundSm=F('background_sm')
        ).values(
            'title', 'text', 'buttonText', 'buttonUrl',
            'backgroundLg', 'backgroundSm')
    )
