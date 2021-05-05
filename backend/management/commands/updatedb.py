from pykml import parser
import requests
from django.core.management.base import BaseCommand, CommandError
from backend.models import Fridge, KmlFile
from django.contrib.gis.geos import Point
from django.utils import timezone
from datetime import timedelta
from django.core.files import File
import kml2geojson
import re
import io

class Command(BaseCommand):
    help = 'Pull data from My Maps\' kml file and update database accordingly'

    def handle(self, *args, **options):
        today = timezone.now()

        KmlFile.objects.all().delete()

        fileName = "myMaps.kml"
        url = 'https://www.google.com/maps/d/u/1/kml?forcekml=1&mid=1hc3fe23eojoXxayFh9kONc6v6ezx558u'
        r = requests.get(url, allow_redirects=True)
        f = io.open(fileName, mode="w", encoding="utf-8")
        f.write(r.text)
        f.close()

        kml2geojson.convert(fileName, "myMapsJson")

        kmlFile = KmlFile()
        with io.open(fileName, mode="r", encoding="utf-8") as f:
            root = parser.parse(f).getroot()
            kmlFile.kml_file.save(fileName, File(f))
            
        with io.open('myMapsJson/myMaps.geojson', mode="r", encoding="utf-8") as f:
            kmlFile.geojson_file.save('myMaps.geojson', File(f))

        kmlFridges = list()

        freeGoFolders = list()

        for folder in root.Document.Folder:
            if re.search("^Nos Free Go.*", str(folder.name)):
                freeGoFolders.append(folder)

        for folder in freeGoFolders:
            for pm in folder.Placemark:
                coords = str(pm.Point.coordinates).strip("\n").strip().split(",")
                name = str(pm.name).rstrip("\n")
                print(str(pm.description).replace("<br>", "\\n"))

                kmlFridges.append({'name': name, 'my_maps_description': str(pm.description).replace("<br>", "\\n"), 'coordinates': Point(float(coords[0]), float(coords[1]))})

        for kmlFridge in kmlFridges:
            qs_closest_fridges = Fridge.objects.filter(coordinates__distance_lte=(kmlFridge['coordinates'], 10)) # Get DB fridges that are less than 10 meters away from kml fridge
            if not qs_closest_fridges:
                new_fridge = Fridge(name=kmlFridge['name'], my_maps_description=kmlFridge['my_maps_description'], coordinates=kmlFridge['coordinates'])
                new_fridge.save()
            elif len(qs_closest_fridges) == 1:
                qs_closest_fridges[0].name = kmlFridge['name']
                qs_closest_fridges[0].my_maps_description = kmlFridge['my_maps_description']
                qs_closest_fridges[0].save()
        
        # Delete fridges that haven't been touched by this script
        db_old_fridges = Fridge.objects.filter(last_modified__lt=today)
        db_old_fridges.delete()

            