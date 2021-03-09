from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    return 'images/{0}'.format(filename)

class Fridge(models.Model):
    def menu_list_default():
        return {"menu": { "name": "", "allergens": ""}}
    
    name = models.CharField(max_length=250)
    my_maps_description = models.TextField(default="My Maps description")
    manager_description = models.TextField(default="Manager description")
    menu_list = models.JSONField(default=menu_list_default)

    def __str__(self):
        return self.name


class Picture(models.Model):
    image = models.ImageField(upload_to=user_directory_path)
    slug = models.SlugField(max_length=250, unique_for_date='created', default='')
    created = models.DateTimeField(default=timezone.now)
    fridge = models.ForeignKey(Fridge, on_delete=models.CASCADE, related_name="pictures")