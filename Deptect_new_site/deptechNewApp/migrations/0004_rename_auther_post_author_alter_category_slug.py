# Generated by Django 4.2.5 on 2023-10-07 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deptechNewApp', '0003_category_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='auther',
            new_name='author',
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
    ]