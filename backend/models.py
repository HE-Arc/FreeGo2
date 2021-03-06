from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django_extensions.db.fields import AutoSlugField

def user_directory_path(instance, filename):
    return 'fridges/{0}'.format(filename)

class Fridge(models.Model):
    def menu_list_default():
        return {'items': [{'name': 'Menu 1', 'children': [{'name': 'cacahouètes'}, {'name': 'lactose'}, ]}, {'name': 'Menu 2', 'children': [{'name': 'lactose'},]}]}
    
    name = models.CharField(max_length=250)
    my_maps_description = models.TextField(default="My Maps description")
    manager_description = models.TextField(default="Manager description")
    menu_list = models.JSONField(default=menu_list_default, blank=True)
    coordinates = models.PointField(default=Point(0, 0), srid=4326, geography=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Picture(models.Model):
    image = models.ImageField(upload_to=user_directory_path)
    created = models.DateTimeField(default=timezone.now)
    slug = AutoSlugField(unique=True, populate_from='image')
    fridge = models.ForeignKey(Fridge, on_delete=models.CASCADE, related_name="pictures")

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fridge = models.ForeignKey(Fridge, on_delete=models.CASCADE)

class Manager(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fridge = models.ForeignKey(Fridge, on_delete=models.CASCADE)

    def __str__(self):
        return self.fridge.name

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fridge = models.ForeignKey(Fridge, on_delete=models.CASCADE)

class KmlFile(models.Model):
    kml_file = models.FileField(upload_to='kml/%Y/%m/%d/')
    geojson_file = models.FileField(upload_to='kml/%Y/%m/%d/', default='')