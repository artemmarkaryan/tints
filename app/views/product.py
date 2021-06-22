from .. import services
from ..models import Sku, Product
import helpers


def get_all_categories(_):
    return helpers.wrap_data({
        'categories': services.product.get_many()
    })


def get_one_category(_, category_id):
    return helpers.wrap_data({
        'categories': services.product.get_many(category_id)
    })


def get_by_sku_id(_, sku_id):
    try:
        return helpers.wrap_data({
            'product': services.product.get_one(sku_id)
        })
    except Sku.DoesNotExist or Product.DoesNotExist:
        return helpers.wrap_error(
            "Продукта не существует",
            404
        )


def get_bestsellers(_):
    return helpers.wrap_data({
        'products': services.product.get_bestsellers()
    })
