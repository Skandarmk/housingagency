# Generated by Django 3.1.1 on 2020-10-04 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_auto_20201004_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='purpose',
            field=models.CharField(choices=[('Residential', 'Residential'), ('Office', 'Office'), ('Business', 'Business'), ('Commercial', 'Commercial'), ('Apartment', 'Apartment'), ('Apartment Building', 'Apartment Building'), ('Condominium', 'Condominium'), ('Single Family Home', 'Single Family Home'), ('Villa', 'Villa')], max_length=50),
        ),
    ]
