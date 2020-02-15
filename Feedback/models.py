from django.db import models
from django.contrib.postgres.fields import ArrayField

class Patient(models.Model):
    mobile_number=models.CharField(max_length=10,primary_key=True,null=False,default=0)
    Rating=models.CharField(max_length=10,null=True,default=None,blank=True)
    sandf=models.CharField(max_length=50,null=True,default=None,blank=False)
    department=models.CharField(max_length=50,null=True,default=None,blank=False)
    AreaofIssue=models.CharField(max_length=40,default=None,null=True,blank=True)
    explanation=models.CharField(max_length=200,null=True,blank=True,default=None)
    recording=models.CharField(max_length=2,null=True,blank=True,default="0")

    def __str__(self):
        return self.mobile_number

class PatientIN(models.Model):
    mobile_number=models.CharField(max_length=10,primary_key=True,null=False,default=0)
    Rating=models.CharField(max_length=10,null=True,default=None,blank=True)
    sandf=models.CharField(max_length=50,null=True,default=None,blank=False)
    department=models.CharField(max_length=50,null=True,default=None,blank=False)
    AreaofIssue=models.CharField(max_length=50,null=True,blank=True,default=None)
    AdmissionIssue=models.CharField(max_length=40,default=None,null=True,blank=True)
    NurseIssue=models.CharField(max_length=40,default=None,null=True,blank=True)
    DoctorIssue=models.CharField(max_length=40,default=None,null=True,blank=True)
    AllotmentIssue=models.CharField(max_length=40,default=None,null=True,blank=True)
    DischargeIssue=models.CharField(max_length=40,default=None,null=True,blank=True)
    explanation=models.CharField(max_length=200,null=True,blank=True,default=None)
    recording=models.CharField(max_length=2,null=True,blank=True,default="0")
    

    def __str__(self):
        return self.mobile_number


class HOD(models.Model):
    email=models.CharField(max_length=100,primary_key=True,default=None)
    password=models.CharField(max_length=20,default=None,blank=False)

    def __str__(self):
        return self.email

