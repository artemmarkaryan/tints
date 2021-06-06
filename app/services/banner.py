from django.db.models import F
from ..models import (
    Banner,
)


def get_all():
    return list(
        Banner.objects.annotate(
            backgorundLg=F('background_lg'),
            backgorundSm=F('background_sm')
        ).values(
            'title', 'text', 'buttonText', 'buttonUrl',
            'backgorundLg', 'backgorundSm')
    )
