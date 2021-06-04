# Generated by Django 3.2.3 on 2021-06-03 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('Наставник', 'Наставник'), ('Модератор(региональный)', 'Модератор(региональный)'), ('Модератор(общий)', 'Модератор(общий)'), ('Администратор', 'Администратор')], default='Наставник', max_length=25, verbose_name='Роль'),
        ),
    ]
