from django.db.models import F, QuerySet

from ..models import (
    Category,
    Product,
    ProductInfo,
    Sku,
    SkuImage,
    SkuVideo
)


def __get_sku_preview_dto(queryset) -> list:
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
        image_query = SkuImage.objects \
            .filter(sku_id=sku[j]['id']) \
            .first()
        if image_query is not None:
            sku[j]['image'] = image_query.image
    return sku


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
        sku[j]['images'] = list(
            SkuImage.objects \
                .filter(sku_id=sku[j]['id']) \
                .values_list('image', flat=True)
        )

    for j in range(len(sku)):
        sku[j]['videos'] = list(
            SkuVideo.objects \
                .filter(sku_id=sku[j]['id']) \
                .values_list('url', flat=True)
        )

    return sku


def get_many(category_id=None):
    if category_id is None:
        categories = list(
            Category.objects
                .annotate(translit=F('translit_name'))
                .values('id', 'name', 'translit')
        )
    else:
        categories = list(
            Category.objects.filter(id=category_id) \
                .annotate(translit=F('translit_name')) \
                .values('id', 'name', 'translit')
        )

    for i, category in enumerate(categories):
        categories[i]['sku'] = __get_sku_preview_dto(
            Sku.objects.filter(
                product__category_id=category['id'],
                hidden=False,
            )
        )

    return categories


def get_one(sku_id):
    sku_query = Sku.objects.filter(id=sku_id)
    if len(sku_query) == 0:
        raise Sku.DoesNotExist

    product_query = Product.objects.filter(id=sku_query[0].product.id) \
        .annotate(
        translit=F('translit_name'),
        categoryId=F('category_id')) \
        .values(
        'id',
        'categoryId',
        'name',
        'translit',
        'description',
    )
    if len(product_query) == 0:
        raise Product.DoesNotExist
    product = product_query.first()
    product['sku'] = __get_sku_dto(sku_query)
    product['info'] = list(
        ProductInfo.objects.filter(product_id=product['id']).values('title',
                                                                    'text'))
    product['related'] = __get_sku_preview_dto(
        Product.objects.get(id=product['id']).related.all()
    )
    return product


def get_bestsellers():
    return __get_sku_preview_dto(
        Sku.objects.filter(product__bestseller=True, hidden=False)
    )
