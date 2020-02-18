from django.contrib import admin
from Feedback.models import Patient,HOD,PatientIN,Minister
# Register your models here.
admin.site.register(Patient)
admin.site.register(HOD)

admin.site.register(PatientIN)
admin.site.register(Minister)
