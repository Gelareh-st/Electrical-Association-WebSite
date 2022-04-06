from django.db import models

# Create your models here.
class WMA(models.Model):
    valid_email:models.EmailField()
    name:models.CharField()