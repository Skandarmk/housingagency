from django.db import models
from django.utils import timezone
from django.utils.text import slugify


import random
from django.conf import settings
import os
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
# Create your models here.

property_type = (
    ('Sale', "sale"),
    ('Rent', "rent")
)

price_category = (
    ('1000 --> 5000 QAR','1000 --> 5000 QAR'),
    ('5000 --> 10000 QAR','5000 --> 10000 QAR'),
    ('10000 --> 15000 QAR','10000 --> 15000 QAR'),
    ('15000 --> 20000 QAR','15000 --> 20000 QAR'),
    ('20000 --> 30000 QAR','20000 --> 30000 QAR'),
    ('30000 --> 50000 QAR','30000 --> 50000 QAR'),
    ('50000 --> 75000 QAR','50000 --> 75000 QAR'),
    ('75000 --> 100000 QAR','75000 --> 100000 QAR'),
    ('100000 --> 125000 QAR','100000 --> 125000 QAR'),
    ('125000 --> 150000 QAR','125000 --> 150000 QAR'),
    ('150000 --> 200000 QAR','150000 --> 200000 QAR'),
    ('200000 --> 1000000 QAR','200000 --> 1000000 QAR'),
    )

STOREY = (
    ('Bungalow', 'Bungalow'),
    ('Duplex', 'Duplex'),
    ('One Storeys', 'One Storeys'),
    ('Two Storeys', 'Two Storeys'),
    ('Three Storeys', 'Three Storeys'),
    ('Four Storeys', 'Four Storeys'),
    ('Five Storeys', 'Five Storeys'),
)



FURNISHED = (
    ('Full Furnished', 'Full Furnished'),
    ('Semi Furnished', 'Semi Furnished'),
    ('None Furnished', 'None Furnished'),
)

NEW_PROPERTY = (
    ('yes', 'yes'),
    ('no', 'no'),
)

PARKING_SPACE = (
    ('yes', 'yes'),
    ('no', 'no'),
)

BEDROOM = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
)

DURATION = (
    ('1 month', '1 month'),
    ('3 months', '3 months'),
    ('6 months', '6 months'),
    ('Year', 'Year'),
    ('2 Years', '2 Years'),
    ('3 Years', '3 Years'),

)

BATHROOM = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
)
PURPOSE = (
    ('Residential', 'Residential'),
    ('Commercial', 'Commercial'),
)


class Property(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    adress = models.CharField( max_length=80)
    type = models.CharField(choices=property_type, max_length=50)
    storey = models.CharField(choices=STOREY, max_length=50)
    furnished = models.CharField(choices=FURNISHED, max_length=50)
    parking_space = models.CharField(choices=PARKING_SPACE, max_length=50)
    new_property = models.CharField(choices=NEW_PROPERTY, max_length=50)
    purpose = models.CharField(choices=PURPOSE, max_length=50)
    duration = models.CharField(choices=DURATION, max_length=50)
    category = models.ForeignKey("Category",null=True , on_delete=models.SET_NULL)
    neighborhood = models.ForeignKey("Neighborhood",default ="2", null=True , on_delete=models.SET_NULL)
    price = models.PositiveIntegerField()
    pricecat = models.CharField(choices=price_category, max_length=50)
    area = models.DecimalField( max_digits=5, decimal_places=2)
    rooms_number = models.PositiveIntegerField()
    beds_number = models.PositiveIntegerField()
    baths_number = models.PositiveIntegerField()
    garages_number = models.PositiveIntegerField()
    image = models.ImageField(upload_to='property/', height_field=None, width_field=None, max_length=None)
    created = models.DateTimeField(default=timezone.now)

    slug = models.SlugField(blank=True  , null=True)

    def save(self , *args , **kwargs):
        if not self.slug and self.name :
            self.slug = slugify(self.name)
        super(Property , self).save(*args , **kwargs)

    class Meta:
        verbose_name = ("Property")
        verbose_name_plural = ("properties")

    def __str__(self):
        return self.name

class PropertyImages(models.Model):
    property = models.ForeignKey(Property , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='propertyimg/' , blank=True , null=True)

    def __str__(self):
        return self.property.name

    class Meta:
        verbose_name = 'Property Image'
        verbose_name_plural = 'Property Images'



class Category(models.Model):
    category_name = models.CharField(max_length=50)
    category_image = models.ImageField(upload_to='category/', height_field=None, width_field=None, max_length=None)

    slug = models.SlugField(blank=True  , null=True)


    def save(self , *args , **kwargs):
        if not self.slug and self.category_name :
            self.slug = slugify(self.category_name)
        super(Category , self).save(*args , **kwargs)


    class Meta:
        verbose_name = ("category")
        verbose_name_plural = ("categories")

    def __str__(self):
        return self.category_name


class Neighborhood(models.Model):
    title        = models.CharField(max_length=120, blank=True, unique=True)
    image        = models.ImageField(upload_to='neighborhoods/', null=True, blank=True)
    slug         = models.SlugField(blank=True,unique=True , null=True)
    category     = models.ForeignKey(Category,blank=True, default=1, max_length=300, unique=False, on_delete=models.CASCADE)


    def save(self , *args , **kwargs):
        if not self.slug and self.title :
            self.slug = slugify(self.title)
        super(Neighborhood , self).save(*args , **kwargs)

    def __str__(self):
        return self.slug




class Reserve(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    notes = models.TextField()

    class Meta:
        verbose_name = ("Reserve")
        verbose_name_plural = ("Reservations")

    def __str__(self):
        return self.name
