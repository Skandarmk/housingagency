# Generated by Django 3.1.1 on 2020-09-29 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20200929_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='desc',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
