# Generated by Django 3.1.1 on 2020-10-04 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_property_neighborhood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='furnished',
            field=models.CharField(choices=[('Full Furnished', 'Full Furnished'), ('Semi Furnished', 'Semi Furnished'), ('None Furnished', 'None Furnished')], max_length=50),
        ),
    ]
