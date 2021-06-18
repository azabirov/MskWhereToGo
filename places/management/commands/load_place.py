from os import path
from django.core.management.base import BaseCommand
from places.models import Place, Coordinates, Image
from django.conf import settings
import requests
from transliterate import slugify
from urllib.parse import urlparse
from pathlib import Path


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

        Coordinates.objects.get_or_create(
            lng=place_raw["coordinates"]["lng"],
            lat=place_raw["coordinates"]["lat"],
            place=place_,
        )

        for index, img_ in enumerate(place_raw["imgs"], 1):
            filename = Path(urlparse(img_).path).name
            filepath = path.join(settings.MEDIA_ROOT, filename)
            response = requests.get(img_, timeout=2.5)
            response.raise_for_status()

            with open(filepath, 'wb') as f:
                f.write(response.content)

            Image.objects.get_or_create(
                post=place_,
                position=index,
                defaults={
                    'img': filename,
                }
            )
