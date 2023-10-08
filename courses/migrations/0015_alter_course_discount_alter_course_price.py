# Generated by Django 4.2.5 on 2023-10-04 09:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_remove_course_offer_price_course_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='discount',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
