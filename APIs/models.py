from tabnanny import verbose
from django.db import models
#Handle the Event Model By Rest framework

class Event(models.Model):
    """
        contains:
            Title
            description
            Poster
            Proposal File(URL)
            retgistration date
            Start Date
            created Date
            Update Date
        Events at the faculty
    """
    Title = models.CharField(max_length=50)
    Decription = models.TextField(blank=True)
    Poster = models.URLField("Poster", max_length=200, blank=True)
    Proposal = models.URLField("Proposal", max_length=200, blank=True)
    registry_start = models.DateTimeField("Registry_Starts?", auto_now=False, blank=True)
    registry_end = models.DateTimeField("Registry_EndTime?",auto_now=False , blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)