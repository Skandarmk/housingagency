from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField( max_length=50)
    image = models.ImageField(upload_to='services/', height_field=None, width_field=None, max_length=None)
    description = models.TextField()

    class Meta:
        verbose_name = ("service")
        verbose_name_plural = ("services")

    def __str__(self):
        return self.name

