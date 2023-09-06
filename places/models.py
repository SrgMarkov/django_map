from django.db import models
from tinymce.models import HTMLField


class Location(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название', null=True, unique=True)
    description_short = models.TextField(verbose_name='Краткое описание', null=True)
    description_long = HTMLField(verbose_name='Полное описание', null=True)
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title


class Picture(models.Model):
    number = models.AutoField(verbose_name='Номер картинки', primary_key=True, unique=True)
    location = models.ForeignKey(Location, verbose_name='Локация', related_name='image', on_delete=models.DO_NOTHING, null=True)
    image = models.ImageField(verbose_name='Изображение')
    picture_order = models.PositiveIntegerField(verbose_name='Позиция', default=0)

    class Meta:
        ordering = ['picture_order']

    def __str__(self):
        return f'{self.number} - {self.location}'
