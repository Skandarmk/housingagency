from django.db import models

# Create your models here.



class About(models.Model):
    vision = models.TextField() 
    mission = models.TextField()
    image =models.ImageField(upload_to='about/', height_field=None, width_field=None, max_length=None)
    


    def __str__(self):
        return str(self.id)
