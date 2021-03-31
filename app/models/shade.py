from django.db.models import *
from .model_with_image import ModelWithImage
import helpers


class Shade(ModelWithImage):
    name = CharField(verbose_name='Название', max_length=512)
