from django.contrib import admin
from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'description', 'category_name')
    list_filter = ('category_name',)
    search_fields = ('product_name', 'description',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'description')
    list_filter = ('category_name',)
    search_fields = ('category_name',)

