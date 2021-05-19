# Generated by Django 3.2.3 on 2021-05-18 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_alter_city_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('afisha', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['start_at'], 'verbose_name': 'Событие', 'verbose_name_plural': 'События'},
        ),
        migrations.AlterModelOptions(
            name='eventparticipant',
            options={'ordering': ['-event'], 'verbose_name': 'Участник', 'verbose_name_plural': 'Участники'},
        ),
        migrations.RemoveField(
            model_name='event',
            name='booked',
        ),
        migrations.AlterField(
            model_name='event',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='event', to='common.city'),
        ),
        migrations.AlterField(
            model_name='eventparticipant',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='eventparticipant', to='afisha.event'),
        ),
        migrations.AlterField(
            model_name='eventparticipant',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventparticipant', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='eventparticipant',
            constraint=models.UniqueConstraint(fields=('user', 'event'), name='unique_participant'),
        ),
    ]
