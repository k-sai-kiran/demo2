from django.shortcuts import render,redirect
from .forms import PatientCreationForm,PatientUpdationForm,HODCreationForm,UserLoginForm,INPatientUpdationForm,OTPVerifyForm
from . models import Patient,HOD,PatientIN
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from .sound_record import audiorec
from scipy.io.wavfile import write
from django.core.mail import send_mail
import math,random
#from django.generic.views import CreateView


def homepage(request):
    return render(request,"Feedback/homepage.html")

def dashboard(request):
    return render(request,'Feedback/dashboard.html')


def addHOD(request):
    if request.method=='POST':
        form=HODCreationForm(request.POST)
        if form.is_valid():
            hod_email=form.cleaned_data['email']
            passwd=form.cleaned_data['password']
            record=HOD(email=hod_email,password=passwd)
            record.save()
            return HttpResponseRedirect(reverse('login'))         
        else:
            field_error="Please Check Your Fields"
            return render(request,'Feedback/HODSignUp.html',{'form':form,'field_error':field_error})
    else:
        form=HODCreationForm()
    return render(request,'Feedback/HODSignUp.html',{'form':form})
    
def login(request):
    if request.method=='POST':
        form=UserLoginForm(request.POST)
        if form.is_valid():
            hod_email=form.cleaned_data['email']
            passwd=form.cleaned_data['password']
            in_HOD=HOD.objects.filter(email=hod_email,password=passwd)
            if in_HOD.exists():
                request.session['admin_ses']=hod_email
                return HttpResponseRedirect(reverse('dashboard'))
            
            else:
                no_account="Your account does not exists"
                return render(request,'Feedback/login.html',{'form':form,'no_account':no_account})         
        else:
            field_error="Invalid Fields"
            return render(request,'Feedback/login.html',{'form':form,'field_error':field_error})

    else:
        form=UserLoginForm()
    return render(request,'Feedback/login.html',{'form':form})


def askingpage(request):
    return render(request,"Feedback/askingpage.html")






def patientfeedback(request):
    if request.method=='POST':
        form=PatientCreationForm(request.POST)
        if form.is_valid():
            digits="0123456789"
            OTPcode=""
            for i in range(4) : 
                OTPcode += digits[math.floor(random.random() * 10)]
            user=form.cleaned_data['mobile_number']
            request.session['user_session']=user
            currentuser=request.session['user_session']
            checksOUT=Patient.objects.filter(mobile_number=currentuser)
            checksIN=PatientIN.objects.filter(mobile_number=currentuser)
            if checksOUT.exists():
                had_error="You have already submitted the feedback"
                return render(request,'Feedback/feedbackstart.html',{'form':form,'had_error':had_error})
            elif checksIN.exists():
                had_error="You have already submitted the feedback"
                return render(request,'Feedback/feedbackstart.html',{'form':form,'had_error':had_error})
            record=Patient(mobile_number=user,otp=OTPcode)
            record.save()
            send_mail('OTP for ESIC',
            'Your One Time Password is'+OTPcode,
            '',
            [user])
            return HttpResponseRedirect(reverse('verifyotp'))
        else:
            field_error="Please Check Your Fields"
            return render(request,'Feedback/feedbackstart.html',{'form':form,'field_error':field_error})
    else:
        form=PatientCreationForm()
    return render(request,'Feedback/feedbackstart.html',{'form':form})

def patientINfeedback(request):
    if request.method=='POST':
        form=PatientCreationForm(request.POST)
        if form.is_valid():
            digits="0123456789"
            OTPcode=""
            for i in range(4): 
                OTPcode += digits[math.floor(random.random() * 10)]
            user=form.cleaned_data['mobile_number']
            request.session['user_session']=user
            currentuser=request.session['user_session']
            checksOUT=Patient.objects.filter(mobile_number=currentuser)
            checksIN=PatientIN.objects.filter(mobile_number=currentuser)
            if checksOUT.exists():
                had_error="You have already submitted the feedback"
                return render(request,'Feedback/feedbackinstart.html',{'form':form,'had_error':had_error})
            elif checksIN.exists():
                had_error="You have already submitted the feedback"
                return render(request,'Feedback/feedbackinstart.html',{'form':form,'had_error':had_error})
            record=PatientIN(mobile_number=user,otp=OTPcode)
            record.save()
            send_mail('OTP for ESIC',
            'Your One Time Password is'+OTPcode,
            '',
            [user])
            return HttpResponseRedirect(reverse('verifyotp'))
        else:
            field_error="Please Check Your Fields"
            return render(request,'Feedback/feedbackinstart.html',{'form':form,'field_error':field_error})
    else:
        form=PatientCreationForm()
    return render(request,'Feedback/feedbackinstart.html',{'form':form})




'''def otpgen(request):
    if request.method=="POST":
        form=OTPForm(request.POST)
        if form.is_valid():
            digits="0123456789"
            OTPcode=""
            for i in range(4) : 
                OTPcode += digits[math.floor(random.random() * 10)] 
            emailid=form.cleaned_data['email_id']
            request.session['otp_sess']=emailid
            record=testing(email_id=emailid,otp=OTPcode)
            record.save()
            send_mail('OTP for ESIC',
            'Your One Time Password is'+OTPcode,
            '',
            [emailid])
            return HttpResponseRedirect(reverse('verifyotp'))

        else:
            field_error="Invalid Field"
            return render(request,'Feedback/otp.html',{'form':form,'field_error':field_error})

    else:
        form=OTPForm()
        return render(request,'Feedback/otp.html')'''


def verifyotp(request):
    if request.method=="POST":
        form=OTPVerifyForm(request.POST)
        if form.is_valid():
            otpsubm=form.cleaned_data['otp']
            currentuser=request.session['user_session']
            actual=Patient.objects.filter(mobile_number=currentuser,otp=otpsubm)
            actualin=PatientIN.objects.filter(mobile_number=currentuser,otp=otpsubm)
            if actual.exists():
                return HttpResponseRedirect(reverse('Feedbackform'))
            elif actualin.exists():
                return HttpResponseRedirect(reverse('IPDFeedbackForm'))
            else:
                error_msg="Incorrect OTP"
                return render(request,"Feedback/otpverify.html",{'form':form, 'error_msg':error_msg})
        else:
            error_msg = "Invalid Details"
            return render(request,"Feedback/otpverify.html",{'form':form, 'error_msg':error_msg})
    else:
        form=OTPVerifyForm()
        return render(request,"Feedback/otpverify.html",{'form':form})

'''def verifyotpIN(request):
    if request.method=="POST":
        form=OTPVerifyForm(request.POST)
        if form.is_valid():
            otpsubm=form.cleaned_data['otp']
            currentuser=request.session['user_session']
            actual=PatientIN.objects.filter(mobile_number=currentuser,otp=otpsubm)
            if actual.exists():
                actual.delete()
                return HttpResponseRedirect(reverse('IPDFeedbackForm'))
            else:
                error_msg="Incorrect OTP"
                return render(request,"Feedback/otpverifyin.html",{'form':form, 'error_msg':error_msg})
        else:
            error_msg = "Invalid Details"
            return render(request,"Feedback/otpverifyin.html",{'form':form, 'error_msg':error_msg})
    else:
        form=OTPVerifyForm()
        return render(request,"Feedback/otpverifyin.html",{'form':form})'''



def IPDFeedbackForm(request):
    if request.method=='POST':
        form=INPatientUpdationForm(request.POST)
        if form.is_valid():
            rating=form.cleaned_data['Rating']
            SorF=form.cleaned_data['sandf']
            Dep=form.cleaned_data['department']
            aoi=form.cleaned_data['AreaofIssue']
            admis=form.cleaned_data['AdmissionIssue']
            nursis=form.cleaned_data['NurseIssue']
            doctis=form.cleaned_data['DoctorIssue']
            allotis=form.cleaned_data['AllotmentIssue']
            disch=form.cleaned_data['DischargeIssue']
            Explanation=form.cleaned_data['explanation']
            currentuser=request.session['user_session']
            record=PatientIN.objects.filter(mobile_number=currentuser).update(Rating=rating,sandf=SorF,department=Dep,AreaofIssue=aoi,AdmissionIssue=admis,NurseIssue=nursis,DoctorIssue=doctis,AllotmentIssue=allotis,DischargeIssue=disch,explanation=Explanation)
            record.save()
            try:
                del request.session['user_session']
            except KeyError:
                pass
            return HttpResponseRedirect(reverse('patientfeedback'))         
        else:
            field_error="Please Check Your Fields"
            return render(request,'Feedback/IPDFeedbackform.html',{'form':form,'field_error':field_error})

    else:
        form=INPatientUpdationForm()
    
    return render(request,'Feedback/IPDFeedbackform.html',{'form':form})



def Feedbackform(request):
    if request.method=='POST':
        form=PatientUpdationForm(request.POST)
        if form.is_valid():
            rating=form.cleaned_data['Rating']
            SorF=form.cleaned_data['sandf']
            Dep=form.cleaned_data['department']
            aoi=form.cleaned_data['AreaofIssue']
            hyg=form.cleaned_data['Hygiene']
            docb=form.cleaned_data['DoctorBehaviour']
            waT=form.cleaned_data['WaitingTime']
            phar=form.cleaned_data['Pharmacy']
            nurse=form.cleaned_data['Nurse']
            Explanation=form.cleaned_data['explanation']
            currentuser=request.session['user_session']
            record=Patient.objects.filter(mobile_number=currentuser).update(Rating=rating,sandf=SorF,department=Dep,AreaofIssue=aoi,Hygiene=hyg,DoctorBehaviour=docb,WaitingTime=waT,Pharmacy=phar,Nurse=nurse,explanation=Explanation)
            record.save()
            try:
                del request.session['user_session']
            except KeyError:
                pass
            return HttpResponseRedirect(reverse('patientfeedback'))         
        else:
            field_error="Please Check Your Fields"
            return render(request,'Feedback/Feedbackform.html',{'form':form,'field_error':field_error})

    else:
        form=PatientUpdationForm()
    
    return render(request,'Feedback/Feedbackform.html',{'form':form})



    


def logout(request):
    try:
        del request.session['admin_ses']
    except KeyError:
        pass
    return HttpResponseRedirect(reverse('login'))
