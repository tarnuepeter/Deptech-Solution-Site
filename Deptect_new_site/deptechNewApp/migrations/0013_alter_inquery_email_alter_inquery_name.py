# Generated by Django 4.2.5 on 2023-10-11 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deptechNewApp', '0012_alter_inquery_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquery',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inquery',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
