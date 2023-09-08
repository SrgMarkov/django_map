from django.db import models
from tinymce.models import HTMLField


class Location(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название',
                             unique=True)
    short_description = models.TextField(verbose_name='Краткое описание',
                                         blank=True)
    long_description = HTMLField(verbose_name='Полное описание', blank=True)
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title


class Picture(models.Model):
    location = models.ForeignKey(Location, verbose_name='Локация',
                                 related_name='images',
                                 on_delete=models.DO_NOTHING)
    image = models.ImageField(verbose_name='Изображение')
    picture_order = models.PositiveIntegerField(verbose_name='Позиция',
                                                default=0, blank=True,
                                                db_index=True)

    class Meta:
        ordering = ['picture_order']

    def __str__(self):
        return f'{self.image} - {self.location}'
