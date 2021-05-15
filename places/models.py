from django.db import models
from tinymce.models import HTMLField

class Place(models.Model):
    placeid = models.CharField("ID места", max_length=256, unique=True)
    title = models.CharField("Название", max_length=256)
    description_short = models.TextField("Короткое описание")
    description_long = HTMLField("Длинное описание")

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"

    def __str__(self):
        return f"{self.placeid} {self.title}"


class Coordinates(models.Model):
    lng = models.FloatField("Долгота")
    lat = models.FloatField("Широта")
    place = models.OneToOneField(Place, on_delete=models.CASCADE, verbose_name="Место")

    class Meta:
        verbose_name = "Координаты"
        verbose_name_plural = "Координаты"

    def __str__(self):
        return f"lng:{self.lng}, lat:{self.lat} {self.place}"


class Image(models.Model):
    img = models.ImageField("Изображение")
    post = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name="Место")
    position = models.IntegerField(db_index=True)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
        ordering = ["position"]

    def __str__(self):
        return f"{self.post.placeid} - #{self.id}"

