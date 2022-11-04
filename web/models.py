from dataclasses import fields
from email.policy import default
from time import perf_counter
from tracemalloc import start
from unittest.util import _MAX_LENGTH
from django.db import models
from random import choices
from tabnanny import verbose
from tkinter import CASCADE
from turtle import end_fill, title
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

Performance_choices = (("Like","Like"),
                       ("Dislike", "Dislike"),)

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


"""
Masters Information`s such as Resume Link/ 
Personal Information related to People Model via Foriegn Key
"""

class Master(models.Model):
    role_choices = [('PHD','PHD'), ('Assistant', 'Assistant'), ('Reasearcher', 'Researcher')]
    Info = models.OneToOneField(People, on_delete=models.CASCADE)
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
        return f"{self.Info.name}, {self.Info.created_date}"

class Master_Performance_Vote(models.Model):
    master = models.ForeignKey(Master, on_delete = models.CASCADE)
    vote = models.CharField(max_length = 10, choices = Performance_choices)
    voter = models.TextField(verbose_name="Voter_session", null = True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
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


class Courses(models.Model):
    """
    The all Courses in the faculty
    """
    tendencies = [('Unknown', 'Unknown'),
                  ('Electronics', 'Electronics'), 
                  ('Power & energy', 'Power & energy'),
                  ('Telecommunications', 'Telecommunications'),
                  ('Automation & control', 'Automation & control'),
                  ]
    title = models.CharField(verbose_name="Tilte",
                                    max_length=15)
    description = models.CharField(verbose_name="Description",
                                    max_length=150)
    tendency = models.CharField(max_length = 30, choices = tendencies, default = "Unknown")
    Unit = models.IntegerField(verbose_name="Unit")
    Prerequisite = models.CharField(verbose_name="prerequisite",
                                    max_length=36, default = None, blank=True, null=True)
    Simultaneous = models.CharField(verbose_name="Simultaneous",
                                    max_length=36, default = None,blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
    def __str__(self) :
        return f"{self.title}/ {self.Unit}/ {self.tendency}"

import datetime
class semester_courses(models.Model):
    year = datetime.datetime.now().year
    semester = [(f'{year}_Meher', f'{year}_Meher'),
                (f'{year}_Bahman',f'{year}_Bahman')]
    """
    The Courses in the present , past and feature semesters
    and its notes
    """
    master = models.ForeignKey("Master", verbose_name = "Master", on_delete = models.CASCADE)
    course = models.ForeignKey("Courses", verbose_name= "Courses", on_delete=models.CASCADE)
    notes = models.URLField(verbose_name = "Notes", max_length=200)
    start = models.CharField(verbose_name = "semester", choices = semester, max_length=50)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
    class Meta:
        verbose_name = 'Semester'
        verbose_name_plural = 'semester_courses'
