from questions import models
from django.core.management.base import BaseCommand
import requests

class Command(BaseCommand):
    # python manage.py createtags --help
    help = 'Fill the database'

    def handle(self, *args, **options):
        url = 'https://query.wikidata.org/bigdata/namespace/wdq/sparql'
        query = '''SELECT DISTINCT ?countryLabel ?headOfStateLabel
        {
           ?country wdt:P31 wd:Q6256;
           wdt:P35 ?headOfState .
           SERVICE wikibase:label { bd:serviceParam wikibase:language "ru" }
        }
        ORDER BY ?countryLabel
        LIMIT 100
        '''
        data = requests.get(url, params={'query': query, 'format': 'json'}).json()
        presidents = []
        for item in data['results']['bindings']:
            presidents.append({
                'country': item['countryLabel']['value'],
                'head_of_state': item['headOfStateLabel']['value']})

        for pr in presidents:
            models.State.objects.create(name= pr['country'], head = pr['head_of_state'])
