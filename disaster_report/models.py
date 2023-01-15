from django.db import models

# Create your models here.
class FootballClubs(models.Model):
    name = models.CharField(max_length=200, unique=True)
    attendance = models.IntegerField(blank=True, null=True)
    stadium = models.CharField(max_length=200,blank=True, null=True)
    zipcode = models.CharField(max_length=200,blank=True, null=True)
    city = models.CharField(max_length=200,blank=True, null=True)
    country = models.CharField(max_length=200,blank=True, null=True)
    adress = models.CharField(max_length=200,blank=True, null=True)
    latitude = models.CharField(max_length=200,blank=True, null=True)
    longitude = models.CharField(max_length=200,blank=True, null=True)


    def __str__(self):
        return self.name