from django.db import models

class Fridge(models.Model):
    name = models.CharField(max_length=250)
    #TODO: Add photos, menu list, My Maps' noticeboard, manager's noticeboard

    def __str__(self):
        return self.name