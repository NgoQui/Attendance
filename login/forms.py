from django import forms
from .models import *
from django.contrib.auth.models import User

class student_form(forms.ModelForm):
    name=forms.Char
