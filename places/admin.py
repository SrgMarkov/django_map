from django.contrib import admin
from django.utils.html import format_html
from .models import Location, Picture


class PicturesInline(admin.TabularInline):
    model = Picture
    readonly_fields = ['preview_image']

    def preview_image(self, obj):
        image_resolution = [obj.image.width, obj.image.height]
        output_resolution = [0, 0]
        output_resolution[image_resolution.index(max(image_resolution))] = 200
        output_resolution[image_resolution.index(min(image_resolution))] = \
            (min(image_resolution) * 200) / max(image_resolution)

        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=output_resolution[0],
            height=output_resolution[1]))


@admin.register(Location)
class Locations(admin.ModelAdmin):
    inlines = [
        PicturesInline,
    ]
    list_display = ['title']

