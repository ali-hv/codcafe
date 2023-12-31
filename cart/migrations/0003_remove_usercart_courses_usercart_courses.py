# Generated by Django 4.2.5 on 2023-11-30 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0001_initial"),
        ("cart", "0002_remove_usercart_courses_usercart_courses"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usercart",
            name="courses",
        ),
        migrations.AddField(
            model_name="usercart",
            name="courses",
            field=models.ForeignKey(
                blank=True,
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cart_courses",
                to="courses.course",
            ),
        ),
    ]
