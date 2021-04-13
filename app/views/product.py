from .. import services
import helpers


def get_all_categories(_):
    return helpers.wrap_data({
        'categories': services.product.get_many()
    })


def get_one_category(_, category_id):
    return helpers.wrap_data({
        'categories': services.product.get_many(category_id)
    })


def get_by_id(_, product_id):
    return helpers.wrap_data({
        'product': services.product.get_one(product_id)
    })

def get_bestsellers(_):
    return helpers.wrap_data({
        'products': services.product.get_bestsellers()
    })