from django.contrib import admin
from .models import Fridge, Picture

class PictureInLine(admin.TabularInline):
    model = Picture

class FridgeAdmin(admin.ModelAdmin):
    inlines = [
        PictureInLine,
    ]

@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug')
    prepopulated_fields = {'slug': ('id',), }

admin.site.register(Fridge, FridgeAdmin)