from django.db import models


class Location(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название', null=True)
    description_short = models.TextField(verbose_name='Краткое описание', null=True)
    description_long = models.TextField(verbose_name='Полное описание', null=True)
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title

