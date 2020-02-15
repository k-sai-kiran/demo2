
from django.urls import path
from django.conf.urls import url

from .import views

urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('Feedbackform/',views.Feedbackform,name="Feedbackform"),
    path('patientfeedback/',views.patientfeedback,name="patientfeedback"),
    path('admindashboard/',views.dashboard,name="dashboard"),
    path('HODSignUp/',views.addHOD,name="addHOD"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('IPDFeedbackform/',views.IPDFeedbackForm,name="IPDFeedbackForm"),
    path('askingpage/',views.askingpage,name="askingpage"),
    path('customeraudio/',views.customeraudio,name="customeraudio"),
]
