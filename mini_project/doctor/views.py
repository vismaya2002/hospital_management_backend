
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from patient.models import Booking,PatientDetails
from .serializers import doctorSerializer,bookingSerializer,patientSerializer
from .models import Doctor
from datetime import date
from .otp import sms
from datetime import datetime
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
def ptdetails(request,pk):
    try:
        dataz = PatientDetails.objects.get(pk='#'+pk)
    except PatientDetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        srData = patientSerializer(dataz)
        return Response(srData.data,status=status.HTTP_200_OK)
    
@api_view(['GET'])
def booking(request,pk):
    try:
        dataz = Booking.objects.filter(doctorid='#'+pk,date=date.today())
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
        dataz = Booking.objects.get (pk=pk)
    except Booking.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "PUT":
        srData = bookingSerializer(dataz,data = request.data)
        if srData.is_valid():
            srData.save()
            return Response(srData.data,status=status.HTTP_200_OK)
        return Response(srData.errors,status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def docinout(request,pk,pt):
    # try:
    
    dataz = Booking.objects.filter(doctorid="#"+pk,date=datetime.today()).values()
    docname = dataz[0]['doctorname']
    id = []
    for i in dataz:
        id.append(i['patientid'])
    print(id)
    for i in id:
        dataz = PatientDetails.objects.filter(patientid=i).values()
        print(dataz[0]['contact1'])
        if pt=="in":
            sms('+91'+str(dataz[0]['contact1']),f'{docname} is currently IN')
        else:
            sms('+91'+str(dataz[0]['contact1']),f'{docname} is currently OUT')
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def token_assignment(request,pk):
    dataz = Booking.objects.filter(doctorid='#'+pk,date=date.today()).values()
    dict={}
    for i in range(len(dataz)):
        dict[dataz[i]['patientid']] = dataz[i]['token']

    dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}
    first_key = []
    first_val = []
    print(dict)
    for i in range(len(dict)):
        first_keyz = list(dict)[i]
        first_valz = list(dict.values())[i]
        first_key.append(first_keyz)
        first_val.append(first_valz)
    

    count =1
    for i in first_key:
        print(i)
        onetime = Booking.objects.get(patientid=i,date=datetime.today())
        onetime.token=count
        onetime.save()
        count+=1

    
    return Response(status=status.HTTP_200_OK)