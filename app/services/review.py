from django.db.models import F
from ..models.review import Review


def get_all():
    return list(Review.objects.values(
        'title',
        'author',
        'url',
        'date',
        'description'
    ))
