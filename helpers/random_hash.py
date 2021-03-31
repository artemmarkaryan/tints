import random
import re
from django.conf import settings


def hash_string():
    return "%032x" % random.getrandbits(128)


