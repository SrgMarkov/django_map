from adminsortable2.admin import SortableAdminBase, SortableStackedInline
from django.contrib import admin
from django.utils.html import format_html

from .models import Location, Picture


@admin.register(Picture)
class Pictures(admin.ModelAdmin):
    list_display = ['location', 'image']


class PicturesInline(SortableStackedInline):
    model = Picture
    readonly_fields = ['preview_image']

    def preview_image(self, obj):
        return format_html('<img src="{}", \
            style="max-width: 200px; max-height: 200px">', obj.image.url)


@admin.register(Location)
class Locations(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        PicturesInline,
    ]
    list_display = ['title']
    search_fields = ['title']
