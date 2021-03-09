from django.contrib import admin
from .models import Fridge, Picture

class PictureInLine(admin.TabularInline):
    model = Picture

class FridgeAdmin(admin.ModelAdmin):
    inlines = [
        PictureInLine,
    ]

admin.site.register(Fridge, FridgeAdmin)
admin.site.register(Picture)