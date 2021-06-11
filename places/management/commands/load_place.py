from django.core.management.base import BaseCommand
from places.models import Place, Coordinates, Image
from django.conf import settings
import requests
import wget
from transliterate import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('url')

    def handle(self, *args, **options):
        url = options["url"]
        response = requests.get(url)
        place_raw = response.json()
        response.raise_for_status()

        place_, created = Place.objects.get_or_create(
            title=place_raw["title"],
            defaults={
                'placeid': slugify(place_raw["title"]).replace("-", "_"),
                'description_long': place_raw["description_long"],
                'description_short': place_raw["description_short"],
            }
        )

        coordinate = Coordinates.objects.get_or_create(
            lng=place_raw["coordinates"]["lng"],
            lat=place_raw["coordinates"]["lat"],
            place=place_,
        )

        for index, img_ in enumerate(place_raw["imgs"]):
            image = Image.objects.get_or_create(
                post=place_,
                position=index+1,
                defaults={
                    'img': wget.download(img_, out=settings.MEDIA_ROOT).split("\\")[-1].split("/")[-1],
                }
            )
