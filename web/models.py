from dataclasses import fields
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from random import choices
from tabnanny import verbose
from tkinter import CASCADE
from turtle import title
from unicodedata import category
from django.db import models


"""
"Soheil Mehrizi"
Hi, I have models
I wrote People, Masters, Members, Courses,
The model of People to maintain the information of all individuals fall into the categories of members, faculty and staff
،
And the professors 'model is related to the People' model for some of the information needed, and it itself maintains 
the resume file and the level of satisfaction with the professor.
The member model from the people model receives its complete information from the people model of the member category.
The Courses Model Contains name , tendency, Category, ratio, Optional_Bool
"""
#Category Choices For People Model /The Category Field

Performance_choices = (("Devile","Devile"),
                       ("Idiot", "Idiot"),
                       ("limbo", "limbo"),
                       ("literate", "literate"),
                       ("Lovely", "Lovely"))

class People(models.Model):
    #Unique ID For Each Person
    class Meta:
        verbose_name = 'People'
        verbose_name_plural = 'People'    

    Category_Choices = [
                        ("Member" , "Member"),
                        ("Faculty" , "Faculty"),
                        ("Staff"   , "Staff"),]

                         
    name  = models.CharField(verbose_name="Name",
                                 max_length=30, editable=True,
                                 serialize=True, blank=True, unique=True)
    
    category = models.CharField(verbose_name = "Category", 
                                  max_length=30,
                                  choices = Category_Choices,
                                  default = 'Faculty')
    Picture_URL = models.URLField(verbose_name="Picture",
                                  max_length=200, blank=True)
    EmailAddress= models.EmailField(verbose_name="Email")
    LinkedIn = models.URLField(max_length=80, blank = True)
    GitHub = models.URLField(max_length=80, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}:{self.name}/{self.category}"



class Courses(models.Model):
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
    id = models.AutoField(verbose_name="ID",
                                    primary_key=True)
    title = models.CharField(verbose_name="Tilte",
                                    max_length=15)
    description = models.CharField(verbose_name="Description",
                                    max_length=150)
    Unit = models.IntegerField(verbose_name="Unit")
    Prerequisite = models.CharField(verbose_name="prerequisite",
                                    max_length=36)
    Simultaneous = models.CharField(verbose_name="Simultaneous",
                                    max_length=36)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"""{self.title} / {self.Unit}/ {self.Simultaneous},
        create_Date:{self.created_date}, Update_date:{self.updated_date}"""
"""
Masters Information`s such as Resume Link/ 
Personal Information related to People Model via Foriegn Key
"""

class Master(models.Model):
    role_choices = [('PHD','PHD'), ('Assistant', 'Assistant'), ('Reasearcher', 'Researcher')]
    Info = models.OneToOneField(People, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Courses, blank=True)
    Resume_Link        = models.URLField(verbose_name = "Resume Link",
                                         max_length=200,blank=True)
    role = models.CharField(choices = role_choices, max_length=50, blank = True)
    Performance_result = models.FloatField(verbose_name="Performance",
                                              blank= True, null = True)
    votes = models.IntegerField(verbose_name = "Votes", blank = True, default = 0)
    About = models.TextField(blank=True)
    class Meta:
        db_table = 'web_master'
        managed = True
        verbose_name = 'Master'
        verbose_name_plural = 'Masters'
    def __str__(self):
        return f"{self.Info.name}, {self.Info.created_date}, {self.courses}"

class Master_Performance_Vote(models.Model):
    master = models.ForeignKey(Master, on_delete = models.CASCADE)
    vote = models.CharField(verbose_name="Performance", max_length = 25,
                                           choices = Performance_choices, blank= True)
    class Meta:
        verbose_name = 'Master_Performance_Vote'
        verbose_name_plural = 'Masters_Performance_Votes'

class Members(models.Model): 
    Info = models.OneToOneField(People, on_delete = models.CASCADE)
    position = models.CharField(max_length=50,verbose_name="position", blank=True)
    
    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'
    def __str__(self):
       return f"{self.Info.name}"