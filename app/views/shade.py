from .. import services
import helpers


def get_all(_):
    return helpers.wrap_data({
        'shades': services.shade.get_all()
    })
