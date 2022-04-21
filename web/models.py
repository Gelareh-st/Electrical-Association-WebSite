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
Category_Choices   = (("Member" , "Member"),
                     ("Faculty", "Faculty"),
                     ("Staff"  , "Staff"),
                     )
Performance_choices = (("1", 1),
                       ("2", 2),
                       ("3", 3),
                       ("4", 4),
                       ("5", 5))

class People(models.Model):
    #Unique ID For Each Person
    id          = models.IntegerField(verbose_name="ID",
                                 primary_key=True,
                                 auto_created=True,
                                 unique_for_month=True)
    
    first_name  = models.CharField(verbose_name="First Name",
                                 max_length=30, editable=True,
                                 serialize=True, blank=True)
    
    last_name   = models.CharField(verbose_name = "Last Name", max_length=30, editable=True,
                                 serialize=True, blank=True)
    
    category    = models.CharField(verbose_name = "Category", 
                                  max_length=30,
                                  choices = Category_Choices,
                                  default = 'Faculty')
    Picture_URL = models.URLField(verbose_name="Picture",
                                  max_length=200)
    EmailAddress= models.EmailField(verbose_name="Email")
    LinkedIn    = models.URLField(max_length=80, blank = True)
    GitHub      = models.URLField(max_length=80, blank=True)
    def __str__(self):
        return f"{self.id}:{self.first_name}_{self.last_name}/{self.category}"


"""
Masters Information`s such as Resume Link/ 
Personal Information related to People Model via Foriegn Key
"""
class Master(People):
  #  ID      = models.OneToOneField(People,
   #                                      on_delete=models.CASCADE)
    Resume_Link        = models.URLField(verbose_name = "Resume Link",
                                         max_length=200,)
    Performance_result = models.IntegerField(verbose_name="Performance",
                                             choices=Performance_choices)
    def __str__(self):
        return f"{self.first_name},{self.last_name}"

#prerequisite must get from itself
class Courses(models.Model):
    id           = models.AutoField(verbose_name="ID",
                                    primary_key=True)
    title        = models.CharField(verbose_name="Tilte",
                                    max_length=15)
    description  = models.CharField(verbose_name="Description",
                                    max_length=150)
    Unit         = models.IntegerField(verbose_name="Unit")
    Prerequisite = models.CharField(verbose_name="prerequisite",
                                    max_length=15)
    Simultaneous = models.CharField(verbose_name="Simultaneous",
                                    max_length=15)
    def __str__(self):
        return f"{self.id};{self.title};{self.Unit}"

class given_Course_By_Master(models.Model):
    course = models.OneToOneField(Courses,
                                 verbose_name="course",
                                 on_delete=models.CASCADE)
    master = models.OneToOneField(Master,
                                 verbose_name="Master",
                                 on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.master.first_name} {self.master.first_name} )= {self.course.title}"
class Members(People):
    def __str__(self):
        f"{self.id}/{self.first_name},{self.last_name}/{self.category}"