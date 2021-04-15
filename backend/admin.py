from django.contrib import admin
from django_json_widget.widgets import JSONEditorWidget
from django.db import models
from .models import Fridge, Picture, Favorite, Manager, Notification, KmlFile

class PictureInLine(admin.TabularInline):
    model = Picture

class FridgeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_modified')
    inlines = [
        PictureInLine,
    ]
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }

@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug')

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'fridge', 'fridge_id')

class ManagerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'fridge')

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'fridge')


admin.site.register(Fridge, FridgeAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Manager, ManagerAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(KmlFile)