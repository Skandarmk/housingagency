from django.db import models

# Create your models here.


class Agent(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='agents/', height_field=None, width_field=None, max_length=None)
    

    class Meta:
        verbose_name = ("Agent")
        verbose_name_plural = ("Agents")

    def __str__(self):
        return self.name
