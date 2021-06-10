from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Place, Image, Coordinates


def mainview(request):
    features = []
    for place in Place.objects.all():
        try:
            features.append({
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.coordinates.lng, place.coordinates.lat],
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.placeid,
                    "detailsUrl": reverse(placeview, args=[place.id]),
                }
            })
        except:
            Coordinates.objects.create(place=place)
            features.append({
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.coordinates.lng, place.coordinates.lat],
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.placeid,
                    "detailsUrl": reverse(placeview, args=[place.id]),
                }
            })

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    return render(request, 'index.html', context={'places': geojson})


def placeview(request, pk):
    place = get_object_or_404(Place, id=pk)
    #imgs = [image.img.url for image in Image.objects.filter(post=place)]
    imgs = [image.img.url for image in place.post.all()]
    print(imgs)

    response_data = {
        'title': place.title,
        'imgs': imgs if imgs else None,
        'description_short': place.description_short if place.description_short else None,
        'description_long': place.description_long if place.description_long else None,
        'coordinates': {
            'lat': place.coordinates.lat if place.coordinates.lat else None,
            'lng': place.coordinates.lng if place.coordinates.lng else None,
        }
    }
    return JsonResponse(response_data, json_dumps_params={'indent': 2, 'ensure_ascii': False})
