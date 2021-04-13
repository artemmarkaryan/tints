from .. import services
import helpers


def get_all(_):
    return helpers.wrap_data({
        'banner': services.banner.get_all()
    })
