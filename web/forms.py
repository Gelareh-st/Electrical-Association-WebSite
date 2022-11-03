from dataclasses import fields
from django import forms
from django.forms import ModelForm
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
    year = datetime.datetime.now().year
    semester = [(f'{year}_Meher', f'{year}_Meher'),
                (f'{year}_Bahman',f'{year}_Bahman')]
    master = forms.ChoiceField(choices = Master.objects.all())
    course = forms.ChoiceField(choices = semester_courses.objects.all())
    start = forms.CharField(max_length= 20, choices = semester)
    notes = forms.URLField(max_length=200, blank=True, default=None)
    class Meta:
        model = semester_courses  
        managed = True
        verbose_name = 'Semester_Course'
        verbose_name_plural = 'Semester_Courses'