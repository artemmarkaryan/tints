from .. import services
import helpers


def get_all(_):
    return helpers.wrap_data({
        'categories': services.category.get_all()
    })
