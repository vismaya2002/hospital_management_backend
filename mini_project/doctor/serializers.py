from rest_framework import serializers
from patient.models import Booking,PatientDetails
from .models import Doctor


class doctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class bookingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Booking
        fields = '__all__'

class patientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDetails
        fields = '__all__'
