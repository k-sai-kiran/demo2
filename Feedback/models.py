from django.db import models

class Patient(models.Model):
<<<<<<< HEAD
    mobile_number=models.CharField(max_length=100,null=True,default="0")
    ip_number=models.CharField(max_length=101,null=True,default="0")
=======
    mobile_number=models.CharField(max_length=100,primary_key=True,null=False,default=0)
>>>>>>> 01b223460a761091531d1b4af2d88e5599152d32
    Rating=models.CharField(max_length=10,null=True,default=None,blank=True)
    sandf=models.CharField(max_length=50,null=True,default=None,blank=False)
    department=models.CharField(max_length=50,null=True,default=None,blank=False)
    AreaofIssue=models.CharField(max_length=40,default=None,null=True,blank=True)
    Hygiene=models.CharField(max_length=5,default=None,blank=True,null=True)
    DoctorBehaviour=models.CharField(max_length=5,default=None,blank=True,null=True)
    WaitingTime=models.CharField(max_length=5,default=None,blank=True,null=True)
    Pharmacy=models.CharField(max_length=5,default=None,blank=True,null=True)
    Nurse=models.CharField(max_length=5,default=None,blank=True,null=True)
    explanation=models.CharField(max_length=200,null=True,blank=True,default=None)
    Status=models.CharField(max_length=10,null=True,blank=True,default="0")
    otp=models.CharField(max_length=6,null=True,blank=True,default=None)

    def __str__(self):
        return self.mobile_number

class PatientIN(models.Model):
<<<<<<< HEAD
    mobile_number=models.CharField(max_length=100,null=False,default="0")
    ip_number=models.CharField(max_length=101,null=False,default="0")
=======
    mobile_number=models.CharField(max_length=100,primary_key=True,null=False,default=0)
>>>>>>> 01b223460a761091531d1b4af2d88e5599152d32
    Rating=models.CharField(max_length=10,null=True,default=None,blank=True)
    sandf=models.CharField(max_length=50,null=True,default=None,blank=False)
    department=models.CharField(max_length=50,null=True,default=None,blank=False)
    AreaofIssue=models.CharField(max_length=40,default=None,null=True,blank=True)
    AdmissionIssue=models.CharField(max_length=40,default=None,null=True,blank=True)
    NurseIssue=models.CharField(max_length=40,default=None,null=True,blank=True)
    DoctorIssue=models.CharField(max_length=40,default=None,null=True,blank=True)
    AllotmentIssue=models.CharField(max_length=40,default=None,null=True,blank=True)
    DischargeIssue=models.CharField(max_length=40,default=None,null=True,blank=True)
    explanation=models.CharField(max_length=200,null=True,blank=True,default=None)
    Status=models.CharField(max_length=10,null=True,blank=True,default="0")
    otp=models.CharField(max_length=6,null=True,blank=True,default=None)
    
    def __str__(self):
        return self.mobile_number


class HOD(models.Model):
    email=models.CharField(max_length=100,primary_key=True,default=None)
    password=models.CharField(max_length=20,default=None,blank=False)

    def __str__(self):
        return self.email

class Minister(models.Model):
    email=models.CharField(max_length=100,primary_key=True,default=None)
    password=models.CharField(max_length=20,default=None,blank=False)

    def __str__(self):
        return self.email
        
        
