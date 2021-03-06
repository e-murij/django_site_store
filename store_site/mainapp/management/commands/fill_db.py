from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
import json
import os
from mainapp.models import ProductCategory
from mainapp.models import Product

from authapp.models import ShopUser

JSON_PATH = 'mainapp/jsons'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding='UTF-8') as file:
        return json.load(file)


class Command(BaseCommand):
    def handle(self, *args, **options):

        categories = load_from_json('categories')
        ProductCategory.objects.all().delete()
        for category in categories:
            ProductCategory(**category).save()

        products = load_from_json('products')
        Product.objects.all().delete()
        for product in products:
            category_name = product['category']
            product['category'] = ProductCategory.objects.get(name=category_name)
            Product(**product).save()

        ShopUser.objects.create_superuser(username='admin',password='admin', age=33)