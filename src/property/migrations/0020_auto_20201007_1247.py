# Generated by Django 3.1.1 on 2020-10-07 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0019_auto_20201007_1241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='price_category',
            new_name='pricecat',
        ),
    ]