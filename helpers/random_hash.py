import random
import re
from django.conf import settings


def hash_string():
    return "%032x" % random.getrandbits(128)


def hash_filename(instance, filename):
    extension = filename[filename.rfind('.'):]
    return settings.IMAGES_PATH + hash_string() + extension
