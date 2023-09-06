# Generated by Django 4.2.3 on 2023-09-06 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_alter_location_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='image', to='places.location', verbose_name='Локация'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='picture_order',
            field=models.PositiveIntegerField(default=0, verbose_name='Позиция'),
        ),
    ]