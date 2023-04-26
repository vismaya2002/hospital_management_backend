from django.shortcuts import render
from .models import PatientDetails,Booking
from doctor.models import Doctor
import random



def home(request):
    return render(request,'index.html')

def newpatient(request):
    if request.method == "POST":
        firstname = request.POST.get('firstName')
        lastname = request.POST.get('lastName')
        email = request.POST.get('email')
        address = request.POST.get('address')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        contactnumber = request.POST.get('contactNumber')
        emernumber = request.POST.get('contactNumber1')
        department = request.POST.get('department')
        doctor = request.POST.get('doctor')
        date = request.POST.get('date')
        time = request.POST.get('time')

        idz = "#OR"+str(random.randint(10000,100000))
        patient = PatientDetails(patientid = idz,firstname = firstname,lastname=lastname,email=email,address=address,age=age,gender=gender,contact1=contactnumber,emgnumber=emernumber)
        patient.save()
        doc = Doctor.objects.filter(department=department,doctorname=doctor).values()
        doc_id = doc[0]['doctorid']
        print(doc_id)
        length = 0
        try:
            length = len(Booking.objects.filter(doctorid=doc_id).values())
        except:
            pass
        book = Booking(patientid=idz,doctorid=doc_id,doctorname=doctor,date = date,time=time,token=length+1)
        book.save()
        context = {
            'patientid': idz,
            'firstname': firstname,
            'lastname' : lastname,
            'email' : email,
            'address' : address,
            'gender' : gender,
            'age' : age,
            'contact' : contactnumber,
            'emergency' : emernumber
        }
        return render(request,'patient.html',context)
    
    return render(request,'newpatient.html')

def extpatient(request):
    if request.method == "POST":
        patientid = request.POST.get('patientid')
        patientdetails = PatientDetails.objects.filter(patientid = patientid).values()
        context = {
            'patientid': patientid,
            'firstname': patientdetails[0]['firstname'],
            'lastname' : patientdetails[0]['lastname'],
            'email' : patientdetails[0]['email'],
            'address' : patientdetails[0]['address'],
            'gender' : patientdetails[0]['gender'],
            'age' : patientdetails[0]['age'],
            'contact' : patientdetails[0]['contact1'],
            'emergency' : patientdetails[0]['emgnumber'],
        }
        return render(request,'patient.html',context)
    return render(request,'extpatient.html')

def prescription(request):
    return render(request,'prescription.html')

def booking(request):
    if request.method == "POST":
        patientid = request.POST.get('patientid')
        print(patientid)
        bookingdetails = Booking.objects.filter(patientid=patientid).values()
        context = {
            'bookingdetails' : bookingdetails
        }
        return render(request,'bookings.html',context)
    return render(request,'bookings.html')

def doctors(request):
    return render(request,'doctors.html')

def departments(request):
    return render(request,'depaartments.html')

def contacts(request):
    return render(request,'contact.html')






