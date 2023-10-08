# Generated by Django 4.2.5 on 2023-10-02 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_video_course_alter_course_status_alter_course_videos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='course',
        ),
        migrations.AddField(
            model_name='video',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='video_course', to='courses.course'),
            preserve_default=False,
        ),
    ]
