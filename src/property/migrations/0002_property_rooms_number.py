# Generated by Django 3.1.1 on 2020-09-17 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='rooms_number',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]