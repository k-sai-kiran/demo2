from django import forms
from .import models


class PatientUpdationForm(forms.Form):
    Rating=forms.CharField()
    sandf=forms.CharField()
    department=forms.CharField()
    AreaofIssue=forms.CharField()
    explanation=forms.CharField()

class INPatientUpdationForm(forms.Form):
    Rating=forms.CharField()
    sandf=forms.CharField()
    department=forms.CharField()
    AreaofIssue=forms.CharField()
    explanation=forms.CharField()

class PatientCreationForm(forms.Form):
    mobile_number=forms.CharField()


class HODCreationForm(forms.Form):
    email=forms.CharField()
    password=forms.CharField()

class UserLoginForm(forms.Form):
    email=forms.CharField()
    password=forms.CharField()
    


    
