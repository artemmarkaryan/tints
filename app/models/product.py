from django.db.models import *
from helpers.translit import ru_to_en


class Product(Model):
    name = CharField(verbose_name='Название', max_length=511)
    category = ForeignKey('Category', verbose_name='Категория',
                          on_delete=RESTRICT, null=True)
    translit_name = CharField(verbose_name='Транслит', max_length=511,
                              blank=True)
    description = TextField('Описание')
    new = BooleanField(default=False)
    top = BooleanField(default=False)
    bestseller = BooleanField(verbose_name='Бестселлер', default=False)
    related = ManyToManyField(
        to='Sku',
        related_name='related',
        verbose_name='Также рекомендуем',
        blank=True
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name

    def save(self, *a, **kw):
        self.name = self.name.strip()
        self.translit_name = ru_to_en(self.name)
        super().save()


