# Generated by Django 3.1.1 on 2020-10-01 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_neighborhood_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='neighborhood',
            field=models.ForeignKey(default='2', null=True, on_delete=django.db.models.deletion.SET_NULL, to='property.neighborhood'),
        ),
    ]