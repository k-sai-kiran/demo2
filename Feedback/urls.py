
from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('Feedbackform/',views.Feedbackform,name="Feedbackform"),
    path('patientfeedback/',views.patientfeedback,name="patientfeedback"),
    path('patientINfeedback/',views.patientINfeedback,name="patientINfeedback"),
    path('admindashboard/',views.dashboard,name="dashboard"),
    path('HODSignUp/',views.addHOD,name="addHOD"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('IPDFeedbackform/',views.IPDFeedbackForm,name="IPDFeedbackForm"),
    path('askingpage/',views.askingpage,name="askingpage"),
    #path('otpgen/',views.otpgen,name="otpgen"),
    path('otpverify/',views.verifyotp,name="verifyotp"),

]
