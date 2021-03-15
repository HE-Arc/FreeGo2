from pykml import parser
import requests
from django.core.management.base import BaseCommand, CommandError
from backend.models import Fridge
from django.contrib.gis.geos import Point

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
            coords = str(pm.Point.coordinates).strip("\n").strip().split(",")
            fridge = Fridge(name=pm.name, my_maps_description=pm.description, coordinates=Point(float(coords[0]), float(coords[1])))
            fridge.save()