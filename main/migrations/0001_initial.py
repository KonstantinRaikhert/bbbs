# Generated by Django 3.2.4 on 2021-07-01 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questions', '0001_initial'),
        ('entertainment', '0001_initial'),
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articles', models.ManyToManyField(to='entertainment.Article', verbose_name='Статьи')),
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='places.place', verbose_name='Место - куда пойти?')),
                ('questions', models.ManyToManyField(to='questions.Question', verbose_name='Вопросы')),
            ],
            options={
                'verbose_name': 'Главная страница',
                'verbose_name_plural': 'Главная страница',
            },
        ),
    ]
