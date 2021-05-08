from django.http import HttpResponse
from django.shortcuts import render

from places.models import Place


def test(request):
    places = Place.objects.all()
    return render(request, 'index.html', context={"places": places})


def mainview(request):
    data = []

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
                "detailsUrl": "Hallo! Nothing here",
            }
        })

    geojson = {
        "type": "FeatureCollection",
        "features": data
    }

    return render(request, 'index.html', context={'geojson': geojson})