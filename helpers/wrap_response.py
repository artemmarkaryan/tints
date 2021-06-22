import json
from typing import Any
from django.http import JsonResponse


class JSONEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        try:
            return json.JSONEncoder.default(self, o)
        except TypeError:
            return str(o)


def wrap_data(data: dict):
    return JsonResponse(
        {'data': data},
        encoder=JSONEncoder,
        safe=False
    )


def wrap_error(message: str, status: int = 400):
    return JsonResponse(
        {'error': message},
        encoder=JSONEncoder,
        safe=False,
        status=status
    )
