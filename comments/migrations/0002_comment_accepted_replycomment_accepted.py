# Generated by Django 4.2.5 on 2023-10-25 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='replycomment',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
    ]
