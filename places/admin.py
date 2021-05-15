from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html
from places.models import Coordinates, Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 0
    readonly_fields = ['image_preview']
    verbose_name = 'Превью изображения (возможно перетащить)'

    def image_preview(self, obj):
        if obj.img:
            return format_html('<img src="{}" height="200"/>', obj.img.url)
        else:
            return "Место для превью изображения"


class CoordinatesInline(admin.StackedInline):
    model = Coordinates


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    model = Place
    inlines = [
        CoordinatesInline, ImageInline,
    ]


admin.site.register(Image)