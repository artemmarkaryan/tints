from django.db.models import *


class ProductInfo(Model):
    class Meta:
        verbose_name = "Информация о продукте"
        verbose_name_plural = "Информация о продукте"

    def __str__(self):
        return f"\"{self.title}\" о {self.product.name}"
    product = ForeignKey('Product', verbose_name='Продукт', on_delete=CASCADE)
    title = CharField('Заголовок', max_length=512)
    text = TextField('Текст')
