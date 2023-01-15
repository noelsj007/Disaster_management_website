from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class Disaster_report(models.Model):
    name = models.CharField(max_length=200, unique=True)
    zipcode = models.CharField(max_length=200,blank=True, null=True)
    city = models.CharField(max_length=200,blank=True, null=True)
    country = models.CharField(max_length=200,blank=True, null=True)
    adress = models.CharField(max_length=200,blank=True, null=True)
    latitude = models.CharField(max_length=200,blank=True, null=True)
    longitude = models.CharField(max_length=200,blank=True, null=True)
    location = models.PointField(null=True)
    images = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.name