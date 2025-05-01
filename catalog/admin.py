from django.contrib import admin
from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    idlelib = ('id',)
    list_display = ('product_name', 'price', 'category_name')
    list_filter = ('category_name',)
    search_fields = ('product_name', 'description',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    idlelib = ('id',)
    list_display = ('category_name', 'description')
    list_filter = ('category_name',)
    search_fields = ('category_name', 'description',)

