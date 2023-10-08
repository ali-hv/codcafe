# Generated by Django 4.2.5 on 2023-09-30 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_remove_video_course_course_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='video',
        ),
        migrations.AddField(
            model_name='course',
            name='video',
            field=models.ManyToManyField(default=None, to='courses.video'),
        ),
    ]
