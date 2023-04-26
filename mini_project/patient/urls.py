from django.urls import path
from .views import *

urlpatterns = [
    path('',home),
    path('newpatient/',newpatient),
    path('extpatient/',extpatient),
    path('bookings/',booking),
    path('prescription/',prescription),
    path('doctors/',doctors),
    path('departments/',departments),
    path('contacts/',contacts),
    path('patientbooking/',patientbooking)
]