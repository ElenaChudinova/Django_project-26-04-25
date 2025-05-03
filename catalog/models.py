from django.db import models

class Category(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, verbose_name='id')
    category_name = models.CharField(max_length=50, verbose_name='Наименование')  # наименование,
    description = models.TextField(max_length=300, verbose_name='Описание', null=True, blank=True)  # описание,

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, verbose_name='id')
    product_name = models.CharField(max_length=50, verbose_name='Наименование') # наименование,
    description = models.TextField(max_length=300, verbose_name='Описание', null=True, blank=True) # описание,
    image = models.ImageField(upload_to='media/photos', verbose_name='Фотография', null=True, blank=True) # изображение,
    category_name = models.CharField(max_length=50, verbose_name='Категория') # категория,
    price = models.IntegerField(verbose_name='Цена') # цена за покупку,
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', editable=False) # дата создания,
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения', editable=False) # дата последнего изменения.
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')

    def __str__(self):
        return f'{self.product_name} {self.category_name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['product_name',]