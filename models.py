from django.db import models


class Category(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, verbose_name="id")
    category_name = models.CharField(max_length=50, verbose_name="Наименование")
    description = models.TextField(
        max_length=300, verbose_name="Описание", null=True, blank=True
    )

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Product(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, verbose_name="id")
    product_name = models.CharField(
        max_length=50,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        max_length=300, verbose_name="Описание", null=True, blank=True
    )
    image = models.ImageField(
        upload_to="photos", verbose_name="Фотография", null=True, blank=True
    )
    category_name = models.CharField(max_length=50, verbose_name="Категория")
    price = models.PositiveIntegerField(default=0, verbose_name="Цена")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания", editable=False, blank=True
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата последнего изменения",
        editable=False,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
    )

    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )

    def __str__(self):
        return f"{self.product_name} {self.category_name}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = [
            "product_name",
        ]
