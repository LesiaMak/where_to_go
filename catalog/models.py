from django.db import models


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Короткое описание', blank=True)
    description_long = models.TextField('Расширенное описание', blank=True)
    lng = models.FloatField("Долгота", blank=True)
    lat = models.FloatField("Широта", blank=True)

    def __str__(self):
        return self.title
