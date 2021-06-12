from django.core.management.base import BaseCommand
from places.models import Place, Coordinates, Image
from django.conf import settings
import requests
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
            filename_raw = settings.MEDIA_ROOT + '\\' + img_.split("\\")[-1].split("/")[-1]
            filename_clean = img_.split("\\")[-1].split("/")[-1]
            response = requests.get(img_, timeout=0.5)
            response.raise_for_status()

            with open(filename_raw, 'wb') as f:
                f.write(response.content)

            image = Image.objects.get_or_create(
                post=place_,
                position=index+1,
                defaults={
                    'img': filename_clean,
                }
            )
