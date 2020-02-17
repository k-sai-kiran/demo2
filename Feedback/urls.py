
from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('patientcomplaints/',views.patientcomplaints,name="patientcomplaints"),
    path('patientINcomplaints/',views.patientINcomplaints,name="patientINcomplaints"),
    path('Feedbackform/',views.Feedbackform,name="Feedbackform"),
    path('patientfeedback/',views.patientfeedback,name="patientfeedback"),
    path('patientcomplaints/<patient_id>/',views.change,name="change"),
    path('patientINcomplaints/<patient_id>/',views.change2,name="change2"),
    path('patientcomplaints/<patient_id>/',views.forward,name="forward"),
    path('patientINcomplaints/<patient_id>/',views.forward,name="forward2"),
    path('patientINfeedback/',views.patientINfeedback,name="patientINfeedback"),
    path('admindashboard/',views.dashboard,name="dashboard"),
    path('thankyou/',views.thankyou,name="thankyou"),
    path('HODSignUp/',views.addHOD,name="addHOD"),
    path('MinisterSignUp/',views.addMinister,name="addMinister"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('IPDFeedbackform/',views.IPDFeedbackForm,name="IPDFeedbackForm"),
    path('askingpage/',views.askingpage,name="askingpage"),
    path('adminaskingpage/',views.adminaskingpage,name="adminaskingpage"),
    path('otpverify/',views.verifyotp,name="verifyotp"),

]


