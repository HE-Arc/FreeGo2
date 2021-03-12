from pykml import parser
import requests
from django.core.management.base import BaseCommand, CommandError
from backend.models import Fridge

class Command(BaseCommand):
    help = 'Pull data from My Maps\' kml file and update database accordingly'

    def handle(self, *args, **options):
        fileName = "myMaps.kml"
        url = 'https://www.google.com/maps/d/u/1/kml?forcekml=1&mid=1hc3fe23eojoXxayFh9kONc6v6ezx558u'
        r = requests.get(url, allow_redirects=True)
        f = open(fileName, "w")
        f.write(r.text)
        f.close()

        with open(fileName, 'r') as f:
            root = parser.parse(f).getroot()

        for pm in root.Document.Folder.Placemark:
            fridge = Fridge(name=pm.name, manager_description=pm.description)
            fridge.save()