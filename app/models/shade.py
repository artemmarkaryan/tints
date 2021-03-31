from django.db.models import *
from .model_with_image import ModelWithImage
import helpers

class Shade(ModelWithImage):
    name = CharField(verbose_name='Название', max_length=512)
    image = FileField(
        verbose_name='Фото',
        upload_to=helpers.images.create_image_path,
        null=True, blank=True
    )
    image_url = CharField(
        verbose_name='Ссылка на фото',
        max_length=1023,
        null=True, blank=True
    )
