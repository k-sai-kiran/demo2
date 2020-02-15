from django.shortcuts import render,redirect
from .forms import PatientCreationForm,PatientUpdationForm,HODCreationForm,UserLoginForm,INPatientUpdationForm
from . models import Patient,HOD
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from .sound_record import audiorec
from scipy.io.wavfile import write
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
            user=form.cleaned_data['mobile_number']
            request.session['user_session']=user
            currentuser=request.session['user_session']
            checks=Patient.objects.filter(mobile_number=currentuser)
            if checks.exists():
                had_error="You have already submitted the feedback"
                return render(request,'Feedback/feedbackstart.html',{'form':form,'had_error':had_error})
            record=Patient(mobile_number=user)
            record.save()
            return HttpResponseRedirect(reverse('askingpage'))         
        else:
            field_error="Please Check Your Fields"
            return render(request,'Feedback/feedbackstart.html',{'form':form,'field_error':field_error})
    else:
        form=PatientCreationForm()
    return render(request,'Feedback/feedbackstart.html',{'form':form})




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
            record=Patient.objects.filter(mobile_number=currentuser).update(Rating=rating,sandf=SorF,department=Dep,AreaofIssue=aoi,AdmissionIssue=admis,NurseIssue=nursis,DoctorIssue=doctis,AllotmentIssue=allotis,DischargeIssue=disch,explanation=Explanation)
            try:
                del request.session['user_session']
            except KeyError:
                pass
            return HttpResponseRedirect(reverse('homepage'))         
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
            Explanation=form.cleaned_data['explanation']
            currentuser=request.session['user_session']
            record=Patient.objects.filter(mobile_number=currentuser).update(Rating=rating,sandf=SorF,department=Dep,AreaofIssue=aoi,explanation=Explanation)
            try:
                del request.session['user_session']
            except KeyError:
                pass
            return HttpResponseRedirect(reverse('homepage'))         
        else:
            field_error="Please Check Your Fields"
            return render(request,'Feedback/Feedbackform.html',{'form':form,'field_error':field_error})

    else:
        form=PatientUpdationForm()
    
    return render(request,'Feedback/Feedbackform.html',{'form':form})


def customeraudio(request):
    currentuser=request.session["user_session"]
    soundobj=Patient.objects.filter(mobile_number=currentuser)
    if(soundobj.exists()):
        b=audiorec()
        rec = b.recordaudio()
        write(currentuser+".mp3",b.fs,rec)
        soundobj=Patient.objects.filter(mobile_number=currentuser).update(recording="1")
        
    else:
        return HttpResponseRedirect(reverse('Feedbackform'))
    return HttpResponseRedirect(reverse('Feedbackform'))

    


def logout(request):
    try:
        del request.session['admin_ses']
    except KeyError:
        pass
    return HttpResponseRedirect(reverse('login'))
