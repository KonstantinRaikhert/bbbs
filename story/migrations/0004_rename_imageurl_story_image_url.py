# Generated by Django 3.2.5 on 2021-07-09 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0003_rename_image_story_imageurl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='story',
            old_name='imageUrl',
            new_name='image_url',
        ),
    ]
