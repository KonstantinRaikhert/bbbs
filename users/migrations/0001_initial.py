import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("common", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("mentor", "Mentor"),
                            ("moderator_regional", "Moderator Reg"),
                            ("moderator_general", "Moderator Gen"),
                            ("admin", "Admin"),
                        ],
                        default="mentor",
                        max_length=20,
                    ),
                ),
                (
                    "city",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="common.city",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("mentor", "Mentor"),
                            ("moderator_regional", "Moderator Reg"),
                            ("moderator_general", "Moderator Gen"),
                            ("admin", "Admin"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "city",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="common.city",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("mentor", "Mentor"),
                            ("moderator_regional", "Moderator Reg"),
                            ("moderator_general", "Moderator Gen"),
                            ("admin", "Admin"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "city",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="common.city",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("mentor", "Mentor"),
                            ("moderator_regional", "Moderator Reg"),
                            ("moderator_general", "Moderator Gen"),
                            ("admin", "Admin"),
                        ],
                        default="mentor",
                        max_length=20,
                    ),
                ),
                (
                    "city",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="common.city",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
