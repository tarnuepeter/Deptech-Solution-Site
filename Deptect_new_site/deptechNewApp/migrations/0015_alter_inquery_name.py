# Generated by Django 4.2.5 on 2023-10-11 11:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('deptechNewApp', '0014_alter_inquery_contact_alter_inquery_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquery',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
