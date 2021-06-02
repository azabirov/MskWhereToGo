import os
import django
import json
import requests
import wget
from transliterate import slugify

os.environ['DJANGO_SETTINGS_MODULE'] = 'where_to_go.settings'
django.setup()

from places.models import Coordinates, Place, Image

'''
if __name__ == '__main__':
    with open('static/places/moscow_legends.json', encoding='utf-8') as data_file:
        json_data = json.loads(data_file.read())

    place = Place.objects.create(
        title=json_data["title"],
        placeid='moscow_legends',
        description_long=json_data["description_long"],
        description_short=json_data["description_short"],
        #coordinates=coordinate,
    )

    coordinate = Coordinates.objects.create(
        lng=json_data["coordinates"]["lng"],
        lat=json_data["coordinates"]["lat"],
        post=place,
    )

    for img_ in json_data["imgs"]:
        image = Image.objects.create(
            img=wget.download(img_),
            post=place,
        )

    with open('static/places/roofs24.json', encoding='utf-8') as data_file:
        json_data = json.loads(data_file.read())

        place = Place.objects.create(
            title=json_data["title"],
            placeid='roofs24',
            description_long=json_data["description_long"],
            description_short=json_data["description_short"],
            #coordinates=coordinate,
        )

        coordinate = Coordinates.objects.create(
            lng=json_data["coordinates"]["lng"],
            lat=json_data["coordinates"]["lat"],
            post=place,
        )

        for img_ in json_data["imgs"]:
            image = Image.objects.create(
                img=wget.download(img_),
                post=place,
            )
'''
'''
if __name__ == '__main__':
    images = Image.objects.all()
    for image in images:
        image.position = image.id-40
        image.save()
'''
if __name__ == '__main__':
        objs = Place.objects.all()
        for obj in objs:
            obj.placeid = slugify(obj.title).replace("-", "_")
            obj.save()