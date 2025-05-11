from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import products_list, info_product, index, add_product

app_name = CatalogConfig.name

urlpatterns = [
    path('', products_list, name='products_list'),
    path('add_product/', add_product, name='add_product'),
    path('product/<int:pk>/', info_product, name='info_product'),
    path('index/', index, name='index'),
]
