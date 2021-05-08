from django.contrib import admin

from places.models import Coordinates, Place, Image

admin.site.register(Coordinates)
admin.site.register(Place)
admin.site.register(Image)
