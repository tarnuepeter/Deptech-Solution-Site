# Generated by Django 4.2.5 on 2023-10-07 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deptechNewApp', '0005_post_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='picture',
        ),
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]