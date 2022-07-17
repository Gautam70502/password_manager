from ast import Pass
from dataclasses import field
from pyexpat import model
from django import forms
from . models import Password_Manager

class Appform(forms.ModelForm):
    
    class Meta:
        model = Password_Manager

        fields = [
            "logo",
            "application_name",
            "Email",
            "password",
        ]
