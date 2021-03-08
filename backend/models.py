from django.db import models

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
    image = models.ImageField()
    fridge = models.ForeignKey(Fridge, on_delete=models.CASCADE)