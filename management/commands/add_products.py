from django.core.management.base import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):
    help = 'Удалить, затем добавить продукты в базу данных'

    def handle(self, *args, **options):

        Product.objects.all().delete()

        category, _ = Category.objects.get_or_create(category_name='деликатесы', description='жирность')

        products = [
            {'product_name': 'Молоко', 'price': '169', 'category': category},
            {'product_name': 'Творог', 'price': '259', 'category': category},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.product_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exist: {product.product_name}'))