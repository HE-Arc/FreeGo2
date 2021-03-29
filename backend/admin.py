from django.contrib import admin
from .models import Fridge, Picture, Favorite, Manager

class PictureInLine(admin.TabularInline):
    model = Picture

class FridgeAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_modified')
    inlines = [
        PictureInLine,
    ]

@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug')
    prepopulated_fields = {'slug': ('id',), }

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'fridge')

class ManagerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'fridge')


admin.site.register(Fridge, FridgeAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Manager, ManagerAdmin)