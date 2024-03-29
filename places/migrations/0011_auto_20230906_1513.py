# Generated by Django 4.2.3 on 2023-09-06 15:13

from django.db import migrations

from places.models import Location


def change_none(apps, schema_editor):
    for location in Location.objects.all():
        if location.title is None:
            location.title = ''
        if location.short_description is None:
            location.short_description = ''
        if location.long_description is None:
            location.long_description = ''
        if location.lat is None:
            location.lat = ''
        if location.lng is None:
            location.lng = ''
        location.save()
        

class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_alter_location_lat_alter_location_lng_and_more'),
    ]

    operations = [
        migrations.RunPython(change_none),
    ]
