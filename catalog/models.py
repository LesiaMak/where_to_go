from django.db import models


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Короткое описание', blank=True)
    description_long = models.TextField('Расширенное описание', blank=True)
    lng = models.FloatField("Долгота", blank=True)
    lat = models.FloatField("Широта", blank=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    image_place = models.ForeignKey(Place,
                                    related_name='images',
                                    on_delete=models.CASCADE,
                                    verbose_name='Место с картинки',
                                    )
    image_id = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return f"{self.image_id} {str(self.image_place)}"
