from django.db.models import F
from typing import List, Dict
from ..models import (
    Category,
    Product,
    ProductInfo,
    Sku,
    SkuImage
)


def __get_sku_dto(queryset) -> list:
    sku = list(
        queryset.annotate(
            productId=F('product_id'),
            categoryId=F('product__category_id'),
            name=F('product__name'),
            translit=F('product__translit_name'),
            oldPrice=F('old_price'),
            vendorCode=F('vendor_code'),
            shadeId=F('shade_id')
        ).values(
            'id',
            'productId',
            'categoryId',
            'shadeId',
            'name',
            'translit',
            'vendorCode',
            'oldPrice',
            'price',
            'weight'
        )
    )
    for j in range(len(sku)):
        sku[j]['image'] = SkuImage.objects.filter(sku_id=sku[j]['id']).first().image

    return sku


def get_many(category_id=None):
    if category_id is None:
        categories = list(
            Category.objects.annotate(translit=F('translit_name')).values('id', 'name', 'translit')
        )
    else:
        categories = list(
            Category.objects.filter(id=category_id) \
                .annotate(translit=F('translit_name')) \
                .values('id', 'name', 'translit')
        )

    for i, category in enumerate(categories):
        categories[i]['sku'] = __get_sku_dto(
            Sku.objects.filter(product__category_id=category['id'])
        )

    return categories


def get_one(product_id):
    product_list: List[Dict] = list(
        Product.objects.filter(id=product_id).
        annotate(
            categoryId=F('category_id'),
            translit=F('translit_name'),
        ).values(
            'id',
            'category_id',
            'name',
            'translit',
            'description',
        )
    )
    if len(product_list) == 0:
        raise Product.DoesNotExist
    else:
        product = product_list[0]

    product['sku'] = __get_sku_dto(Sku.objects.filter(product_id=product['id']))
    product['info'] = list(ProductInfo.objects.filter(product_id=product['id']).values('title', 'text'))
    product['related'] = __get_sku_dto(Product.objects.get(id=product_id).related.all())
    return product
