from django.db.models import *
from django.core.management import call_command
import helpers


class ModelWithImage(Model):
    """
    use "image" and "image_url" fields
    """
    def save(self, *a, **kw):
        url = self.__getattribute__('image_url')
        if url:
            self.__setattr__(
                'image',
                helpers.images.download_image_from_source(url)
            )
            self.__setattr__('image_url', None)

        call_command('collectstatic', verbosity=0, interactive=False)
        super().save()