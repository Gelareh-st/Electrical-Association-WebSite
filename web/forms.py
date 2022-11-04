from dataclasses import fields
from django import forms
from django.forms import ModelForm

from web.Auxiliary_functions import choice_Maker
from .models import (
                     Courses,
                     People,
                     Master,
                     Members,
                     semester_courses
                    )

class PeopleForm(ModelForm):
    class Meta:
        model = People
        fields = ["name", "Picture_URL", "EmailAddress",
                  "LinkedIn", "GitHub"]
        fields
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-controll', 'placeholder': 'Name'}),
            
            'Picture_URL': forms.URLInput(attrs={'class':'form-controll', 'placeholder': 'Picture_URL'}),
            'EmailAddress': forms.EmailInput(attrs={'class':'form-controll', 'placeholder': 'Email_Address'}),
            'LinkedIn': forms.URLInput(attrs={'class':'form-controll', 'placeholder': 'LinkedIn'}),
            'GitHub': forms.URLInput(attrs={'class':'form-controll', 'placeholder': 'GitHub'}),
        }
class MasterForm(ModelForm):
    class Meta:
        model = Master
        fields = ["Resume_Link", "About"]
        widgets = {
            'Resume_Link': forms.URLInput(attrs={'class':'form-controll'}),
            'About': forms.Textarea(attrs={'class': 'form-controll'})
        }



class MembersForm(ModelForm):
    class Meta:
        model = Members
        fields = ["position"]
        widgets = {
            'position': forms.TextInput(attrs={'class':'form-controll'}),
        }

class CoursesForm(ModelForm):
    tendency = forms.ChoiceField(choices = Courses.tendencies)
    Unit= forms.IntegerField(max_value=4, min_value=1)
    class Meta:
        model = Courses
        fields = [
            'title', 'description', 'tendency', 'Unit', 'Prerequisite', 'Simultaneous',
                 ]
        widgets = {
            'title':forms.TextInput(attrs = {'class':'form-controll', 'placeholder': 'title'}),
            'description': forms.Textarea(attrs = {'class':'form-controll', 'placeholder': 'description'}),

            
            'Prerequisite':forms.TextInput(attrs = {'class':'form-controll', 'placeholder': 'Prerequisite'}),
            'Simultaneous':forms.TextInput(attrs = {'class':'form-controll', 'placeholder': 'Simultaneous'}),
        }

import datetime
class SemesterForm(ModelForm):
    class Meta:
        model = semester_courses
        fields = ['master', 'course', 'notes', 'start']  
        managed = True
        verbose_name = 'Semester_Course'
        verbose_name_plural = 'Semester_Courses'
