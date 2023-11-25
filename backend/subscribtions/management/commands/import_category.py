import csv

from django.core.management.base import BaseCommand

from subscribtions.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        csv_file = open('C:/Users/blwol/PycharmProjects/subscribtion_group_pro'
                        'ject/backend/subscribtions/management/commands/'
                        'category.csv',
                        encoding='utf-8')
        reader = csv.reader(csv_file, delimiter=',')
        next(reader, None)
        list_category = []
        for row in reader:
            name, slug = row
            list_category.append(Category(
                name=name,
                slug=slug))
        Category.objects.bulk_create(list_category)
        print('Категории +')
