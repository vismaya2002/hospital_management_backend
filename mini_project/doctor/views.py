
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from patient.models import Booking
from .serializers import doctorSerializer,bookingSerializer
from .models import Doctor

# Create your views here.

@api_view(['GET'])
def details(request,pk):
    try:
        dataz = Doctor.objects.get(pk='#'+pk)
    except Doctor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        srData = doctorSerializer(dataz)
        return Response(srData.data,status=status.HTTP_200_OK)
    
@api_view(['GET'])
def booking(request,pk):
    try:
        dataz = Booking.objects.filter(doctorid='#'+pk)
    except Booking.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        srData = bookingSerializer(dataz,many=True)
        return Response(srData.data,status=status.HTTP_200_OK)


@api_view(['GET'])
def history(request,pk,pt):
    try:
        dataz = Booking.objects.filter(doctorid='#'+pk,patientid='#'+pt)
    except Booking.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
    
        srData = bookingSerializer(dataz,many=True)
        return Response(srData.data,status=status.HTTP_200_OK)

@api_view(['PUT'])
def checkup(request,pk):
    try:
        dataz = Booking.objects.get(pk=pk)
    except Booking.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "PUT":
        srData = bookingSerializer(dataz,data = request.data)
        if srData.is_valid():
            srData.save()
            return Response(srData.data,status=status.HTTP_200_OK)
        return Response(srData.errors,status = status.HTTP_400_BAD_REQUEST)