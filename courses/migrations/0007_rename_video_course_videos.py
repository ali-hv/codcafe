# Generated by Django 4.2.5 on 2023-09-30 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_remove_course_video_course_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='video',
            new_name='videos',
        ),
    ]
