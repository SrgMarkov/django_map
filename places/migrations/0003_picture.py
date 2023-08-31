# Generated by Django 4.2.4 on 2023-08-24 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_rename_maplocations_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('number', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='Номер картинки')),
                ('image', models.ImageField(upload_to='')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.location')),
            ],
        ),
    ]