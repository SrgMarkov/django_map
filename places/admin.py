from django.contrib import admin
from .models import Location, Picture


class PicturesInline(admin.TabularInline):
    model = Picture


@admin.register(Location)
class Locations(admin.ModelAdmin):
    inlines = [
        PicturesInline,
    ]
    list_display = ['title']