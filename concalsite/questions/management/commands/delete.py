from questions import models
from django.core.management.base import BaseCommand
import random

class Command(BaseCommand):
    # python manage.py createtags --help
    help = 'To delete all records'

    def handle(self, *args, **options):
        my = [1, 2, 3, 4, 5, 6]
        temp = my.copy()
        temp.remove(2)
        l = random.sample(list(temp), 4)
        print(temp)
        print(my)
        temp.remove(5)
        print(temp)
        print(my)