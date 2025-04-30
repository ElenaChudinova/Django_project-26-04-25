from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=50, verbose_name='Наименование') # наименование,
    description = models.TextField(max_length=300, verbose_name='Описание', null=True, blank=True) # описание,
    image = models.ImageField(upload_to='photos/', verbose_name='Фотография', null=True) # изображение,
    category_name = models.CharField(max_length=50, verbose_name='Категория') # категория,
    price = models.IntegerField(max_length=6, verbose_name='Цена') # цена за покупку,
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', editable=False) # дата создания,
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения', editable=False) # дата последнего изменения.

    def __str__(self):
        return f'{self.product_name} {self.category_name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['product_name',]


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Наименование')  # наименование,
    description = models.TextField(max_length=300, verbose_name='Описание', null=True, blank=True)  # описание,
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['category_name', ]