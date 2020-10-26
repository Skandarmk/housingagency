# Generated by Django 3.1.1 on 2020-09-29 18:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_reserve'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='property',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='PropertyImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='propertyimg/')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.property')),
            ],
            options={
                'verbose_name': 'Property Image',
                'verbose_name_plural': 'Property Images',
            },
        ),
    ]