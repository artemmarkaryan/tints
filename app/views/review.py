from ..services import review as review_service
import helpers


def get_all(_):
    return helpers.wrap_data(
        {"reviews": review_service.get_all()}
    )
