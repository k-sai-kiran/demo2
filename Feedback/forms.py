from django import forms
from .import models
from nocaptcha_recaptcha.fields import NoReCaptchaField

# Creating form classes 

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
<<<<<<< HEAD
    ip_number=forms.CharField()
=======
>>>>>>> 01b223460a761091531d1b4af2d88e5599152d32
    captcha = NoReCaptchaField(gtag_attrs={'data-theme':'dark'})



class AdminCreationForm(forms.Form):
    email=forms.CharField()
    password=forms.CharField()
    


class UserLoginForm(forms.Form):
    email=forms.CharField()
    password=forms.CharField()



class OTPVerifyForm(forms.Form):
    otp=forms.CharField()
    


    
