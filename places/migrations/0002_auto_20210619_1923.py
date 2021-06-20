# Generated by Django 3.2.4 on 2021-06-19 19:23

from django.db import migrations, models
import places.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='imageUrl',
            field=models.ImageField(blank=True, help_text='Добавить фото', null=True, upload_to=places.models.get_upload_path, verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='place',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='tags', to='places.PlaceTag', verbose_name='Теги'),
        ),
    ]
