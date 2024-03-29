# Generated by Django 4.2.3 on 2023-09-06 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0012_alter_picture_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='number',
        ),
        migrations.AddField(
            model_name='picture',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='picture',
            name='picture_order',
            field=models.PositiveIntegerField(blank=True, db_index=True, default=0, verbose_name='Позиция'),
        ),
    ]
