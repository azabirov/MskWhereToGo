from django.contrib import admin
from nested_admin.nested import NestedStackedInline, NestedModelAdmin

from places.models import Coordinates, Place, Image
import nested_admin


class ImageInline(admin.StackedInline):
    model = Image


class CoordinatesInline(admin.StackedInline):
    model = Coordinates


class PlaceAdmin(admin.ModelAdmin):
    model = Place
    inlines = [
        CoordinatesInline, ImageInline,
    ]
    #fields = ('placeid','title','description_short','description_long','coordinates')

#admin.site.register(Coordinates)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Image)