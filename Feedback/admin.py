from django.contrib import admin
from Feedback.models import Patient,HOD,PatientIN
# Register your models here.
admin.site.register(Patient)
admin.site.register(HOD)

admin.site.register(PatientIN)
