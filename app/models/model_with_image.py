from django.db.models import *
from django.core.management import call_command
import helpers


class ModelWithImage(Model):
    """
    use "image" and "image_url" fields
    """
    image = FileField('Файл изображения', null=True, blank=True)
    image_url = URLField('Ссылка на изображение', null=True, blank=True)

    def save(self, *a, **kw):
        url = self.image_url
        if url:
            self.image = helpers.images.download_image_from_source(url)
            self.image_url = None

        call_command('collectstatic', verbosity=0, interactive=False)
        super().save()