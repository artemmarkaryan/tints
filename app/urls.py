from django.urls import path
from django.conf import settings
from app.views import (
    product,
    category,
    shade,
    banner,
    feedback,
    newsletter,
    review,
    order,
    shipping_method,
    pay,
    payment_method
)

urlpatterns = [
    path('product/all', product.get_all_categories),
    path('product/<int:sku_id>', product.get_by_sku_id),
    path('product/bestsellers', product.get_bestsellers),
    path('product/category/<int:category_id>', product.get_one_category),
    path('category/all/preview', category.get_all),
    path('shade/all/', shade.get_all),
    path('banner/all/', banner.get_all),
    path('review/all/', review.get_all),
    path('feedback/', feedback.process),
    path('newsletter/', newsletter.process),
    path('order/', order.create),
    path('order/<int:order_id>/pay', order.pay),
    path('order/<int:order_id>', order.get),
    path('shippingMethod/all', shipping_method.get_all),
    path('paymentMethod/all', payment_method.get_all),

    path(settings.PAYMENT_NOTIFICATION_PATH, order.payment_notification)
]
