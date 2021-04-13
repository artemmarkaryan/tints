from django.contrib import admin
from ..models import (
    Shade
)


@admin.register(Shade)
class SahdeAdmin(admin.ModelAdmin):
    pass
