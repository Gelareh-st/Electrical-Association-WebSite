from django import forms
from django.forms import ModelForm
from .models import (People,
                     Master,
                     Members
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
        fields = ["Resume_Link"]
        widgets = {
            'Resume_Link': forms.URLInput(attrs={'class':'form-controll'}),
        }



class MemberForm(ModelForm):
    class Meta:
        model = Members
        fields = ["position"]
        widgets = {
            'position': forms.TextInput(attrs={'class':'form-controll'}),
        }