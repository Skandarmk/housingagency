# Generated by Django 3.1.1 on 2020-10-01 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20201001_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='neighborhood',
        ),
    ]
