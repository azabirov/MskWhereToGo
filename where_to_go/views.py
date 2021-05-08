from django.http import HttpResponse
from django.shortcuts import render

from places.models import Place


def test(request):
    places = Place.objects.all()
    return render(request, 'index.html', context={"places": places})