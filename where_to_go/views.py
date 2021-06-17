from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Place, Coordinates


def main_view(request):
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
                    "detailsUrl": reverse(place_view, args=[place.id]),
                }
            })
        except Coordinates.DoesNotExist:
            continue

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    return render(request, 'index.html', context={'places': geojson})


def place_view(request, pk):
    place = get_object_or_404(Place, id=pk)
    imgs = [request.build_absolute_uri(image.img.url) for image in place.images.all()]

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
