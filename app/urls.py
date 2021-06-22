from django.urls import path
from app.views import (
    product,
    category,
    shade,
    banner,
    feedback,
    newsletter,
    review
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
]
