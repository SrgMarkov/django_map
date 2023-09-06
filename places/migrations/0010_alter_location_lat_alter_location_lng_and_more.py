# Generated by Django 4.2.3 on 2023-09-06 15:11

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_rename_description_long_location_long_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='lat',
            field=models.FloatField(blank=True, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='location',
            name='lng',
            field=models.FloatField(blank=True, verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='location',
            name='long_description',
            field=tinymce.models.HTMLField(blank=True, default='', verbose_name='Полное описание'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='location',
            name='short_description',
            field=models.TextField(blank=True, default='', verbose_name='Краткое описание'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='location',
            name='title',
            field=models.CharField(blank=True, default='', max_length=100, unique=True, verbose_name='Название'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='picture',
            name='location',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, related_name='image', to='places.location', verbose_name='Локация'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='picture',
            name='picture_order',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Позиция'),
        ),
    ]