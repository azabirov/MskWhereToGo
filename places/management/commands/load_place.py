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
        link = requests.get(url)
        json_data = link.json()

        place_, created = Place.objects.get_or_create(
            placeid=slugify(json_data["title"]).replace("-", "_"),
            title=json_data["title"],
            description_long=json_data["description_long"],
            description_short=json_data["description_short"],
        )

        coordinate = Coordinates.objects.get_or_create(
            lng=json_data["coordinates"]["lng"],
            lat=json_data["coordinates"]["lat"],
            place=place_,
        )
        count = 0
        for img_ in json_data["imgs"]:
            count += 1
            image = Image.objects.get_or_create(
                img=wget.download(img_, out=settings.MEDIA_ROOT).split("\\")[-1].split("/")[-1],
                post=place_,
                position=count,
            )