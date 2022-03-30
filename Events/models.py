from django.db import models

# Create your models here.
class Event(models.Model):
    start_date: models.CharField()
    reg_start_time: models.DateTimeField()
    reg_end_time: models.DateTimeField()
    title: models.CharField()
    details:models.TextField()
    reg_links: models.URLField() 
    remain_time: models.TimeField()
    left_time: models.TimeField()
    