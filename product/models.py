from django.db import models


# Create your models here.

class product(models.Model):
    name = models.CharField(max_length=255,null=True)
    image = models.ImageField(null=True,blank=True,upload_to='image/')
    descriotion = models.TextField(max_length=3000)


    def __str__(self):
        return self.name

