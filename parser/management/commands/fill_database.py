from django.core.management.base import BaseCommand
from parser.models import Item

class Command(BaseCommand):
    help = 'Заполняет базу данных тестовыми данными'

    def handle(self, *args, **kwargs):
        # Пример данных
        items = [
            {'name': 'Item 1', 'description': 'Description for item 1'},
            {'name': 'Item 2', 'description': 'Description for item 2'},
            {'name': 'Item 3', 'description': 'Description for item 3'},
        ]

        for item in items:
            Item.objects.create(**item)

        self.stdout.write(self.style.SUCCESS('База данных успешно заполнена'))
