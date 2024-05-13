from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read():
        with open('catalog.json', 'r', encoding='utf8') as file:
            data = json.load(file)
            return data

    def handle(self, *args, **options):
        product_for_create = []
        category_for_create = []

        for i in Command.json_read():
            if i['models'] == 'catalog.category':
                category_for_create.append(
                    Category(name=i.get('fields').get('name'), pk=i.get('pk'),
                             description=i.get('fields').get('description'))
                )
            elif i['models'] == 'catalog.product':
                product_for_create.append(
                    Product(pk=i.get('pk'), name=i.get('fields').get('name'),
                            description=i.get('fields').get('description'), image=i.get('fields').get('image'),
                            category=Category.objects.get(pk=i.get('pk')), price=i.get('fields').get('price'),
                            created_at=i.get('fields').get('created_at'), updated_at=i.get('fields').get('updated_at')
                            )
            Category.objects.bulk_create(category_for_create)

            Product.objects.bulk_create(product_for_create)
