from django.urls import path
from app.views import (
    product,
    category,
    shade,
    banner
)

urlpatterns = [
    path('product/all', product.get_all_categories),
    path('product/<int:product_id>', product.get_by_id),
    path('product/bestsellers', product.get_bestsellers),
    path('product/category/<int:category_id>', product.get_one_category),
    path('category/all/preview', category.get_all),
    path('shade/all/', shade.get_all),
    path('banner/all/', banner.get_all),
]
