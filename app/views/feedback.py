import helpers
from django.views.decorators.http import require_http_methods


@require_http_methods(["POST"])
def process(r):
    return helpers.wrap_data({})
