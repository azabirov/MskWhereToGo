from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Place, Image


def mainview(request):
    data = []
    placeholder = "Hallo! Nothing here"
    for place in Place.objects.all():
        data.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.coordinates.lng, place.coordinates.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.placeid,
                "detailsUrl": reverse(placeview, args=[place.id]),
            }
        })

    geojson = {
        "type": "FeatureCollection",
        "features": data
    }

    return render(request, 'index.html', context={'places': geojson})


def placeview(request, pk):
    place = get_object_or_404(Place, id=pk)
    imgs = [image.img.url for image in Image.objects.filter(post=place)]
    response_data = {
        'title': place.title,
        'imgs': imgs,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.coordinates.lat,
            'lng': place.coordinates.lng,
        }
    }
    return JsonResponse(response_data, json_dumps_params={'indent': 2, 'ensure_ascii': False})
