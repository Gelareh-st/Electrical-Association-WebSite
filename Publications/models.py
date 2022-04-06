from django.db import models

# Create your models here.
class Publications(models.Model):
    title: models.CharField(max_lenght=100)
    img : models.ImageField()
    Link: models.URLField()
    Date: models.CharField(max_length=30)
    Authors: models.CharField(max_length=100)