# Generated by Django 3.2.5 on 2021-07-09 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_merge_0002_alter_place_tags_0006_alter_place_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='imageUrl',
            new_name='image_url',
        ),
    ]
