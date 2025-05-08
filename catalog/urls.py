from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import products_list, contacts, info_product, index

app_name = CatalogConfig.name

urlpatterns = [
    path('', products_list, name='products_list'),
    path('', contacts, name='contacts'),
    path('info_product/<int:pk>/', info_product, name='info_product'),
    path('', index, name='index'),
]
