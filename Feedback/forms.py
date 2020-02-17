from django import forms
from .import models


class PatientUpdationForm(forms.Form):
    Rating=forms.CharField(required=False)
    sandf=forms.CharField(required=False)
    department=forms.CharField(required=False)
    AreaofIssue=forms.CharField(required=False)
    Hygiene=forms.CharField(required=False)
    DoctorBehaviour=forms.CharField(required=False)
    WaitingTime=forms.CharField(required=False)
    Pharmacy=forms.CharField(required=False)
    Nurse=forms.CharField(required=False)
    explanation=forms.CharField(required=False)

class INPatientUpdationForm(forms.Form):
    Rating=forms.CharField(required=False)
    sandf=forms.CharField(required=False)
    department=forms.CharField(required=False)
    AreaofIssue=forms.CharField(required=False)
    AdmissionIssue=forms.CharField(required=False)
    NurseIssue=forms.CharField(required=False)
    DoctorIssue=forms.CharField(required=False)
    AllotmentIssue=forms.CharField(required=False)
    DischargeIssue=forms.CharField(required=False)
    explanation=forms.CharField(required=False)

class PatientCreationForm(forms.Form):
    mobile_number=forms.CharField()


class AdminCreationForm(forms.Form):
    email=forms.CharField()
    password=forms.CharField()
    


class UserLoginForm(forms.Form):
    email=forms.CharField()
    password=forms.CharField()

'''class OTPForm(forms.Form):
    email_id=forms.CharField()'''

class OTPVerifyForm(forms.Form):
    otp=forms.CharField()
    


    
