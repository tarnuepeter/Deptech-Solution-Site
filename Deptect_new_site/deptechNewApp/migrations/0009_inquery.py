# Generated by Django 4.2.5 on 2023-10-09 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deptechNewApp', '0008_alter_post_header_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inquery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('contact', models.IntegerField()),
                ('subject', models.CharField(max_length=300)),
                ('message', models.TextField()),
            ],
        ),
    ]
