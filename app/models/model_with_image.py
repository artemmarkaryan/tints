from django.db.models import *
from django.core.management import call_command
import helpers


class ModelWithImage(Model):
    """
    use "image" and "image_url" fields
    """
    image = FileField('Файл изображения',
                      upload_to=helpers.random_hash.hash_filename,
                      null=True, blank=True)
    image_url = URLField('Ссылка на изображение', null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *a, **kw):
        url = self.image_url
        if url:
            self.image = helpers.images.download_image_from_source(url)
            self.image_url = None

        call_command('collectstatic', verbosity=0, interactive=False)
        super().save()
