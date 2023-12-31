# Generated by Django 4.2.5 on 2023-12-06 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("courses", "0001_initial"),
        ("cart", "0007_alter_usercart_user_delete_cartcourse"),
    ]

    operations = [
        migrations.CreateModel(
            name="TemporaryOrder",
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
                ("tracking_code", models.CharField(max_length=16)),
                (
                    "courses",
                    models.ManyToManyField(
                        blank=True,
                        related_name="temporary_order_courses",
                        to="courses.course",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_temporary_order",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
