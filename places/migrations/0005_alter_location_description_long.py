# Generated by Django 4.2.4 on 2023-09-04 05:59

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_alter_picture_options_picture_picture_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='description_long',
            field=tinymce.models.HTMLField(null=True, verbose_name='Полное описание'),
        ),
    ]
