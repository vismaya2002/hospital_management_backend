from django.contrib import admin
from .models import PatientDetails,Booking,Otp

admin.site.register(PatientDetails)
admin.site.register(Booking)
admin.site.register(Otp)

