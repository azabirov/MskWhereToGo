from django.db import models


class Coordinates(models.Model):
    lng = models.FloatField()
    lat = models.FloatField()


class Place(models.Model):
    placeid = models.CharField(max_length=256, unique=True)
    title = models.CharField(max_length=256)
    description_short = models.TextField()
    description_long =models.TextField()
    coordinates = models.OneToOneField(Coordinates, on_delete=models.CASCADE)


class Image(models.Model):
    img = models.ImageField()
    post = models.ForeignKey(Place, on_delete=models.CASCADE)

