import json
import os
from django.core.management.base import BaseCommand
from places.models import Place, Coordinates, Image
from django.conf import settings
import requests
import wget
import re
from transliterate import slugify

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('url')

    def handle(self, *args, **options):
        url = options["url"]
        link = requests.get(url)
        json_data = link.json()
        #raw_name = link.headers['content-disposition']
        #json_name = os.path.splitext(re.findall("filename=(.+)", raw_name)[0])[0]

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
        count = 1
        for img_ in json_data["imgs"]:
            count += 1
            image = Image.objects.get_or_create(
                img=wget.download(img_, out=settings.MEDIA_ROOT),
                post=place_,
                position=count,
            )