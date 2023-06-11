from django.contrib import admin
from .models import PatientDetails,Booking,Otp,HealthRecord

admin.site.register(PatientDetails)
admin.site.register(Booking)
admin.site.register(Otp)
admin.site.register(HealthRecord)
