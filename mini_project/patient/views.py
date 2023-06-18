from django.shortcuts import render,redirect,HttpResponse
from .models import PatientDetails,Booking,Otp
from doctor.models import Doctor
import random
import datetime
from .otp import sms
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
        otp = random.randint(10000,1000000)
        
        sms("+91"+ str(contactnumber),'your otp is '+str(otp))
        onetime = Otp(patientid=idz,otp=otp)
        onetime.save() 
        context = {
            'firstname' : firstname,
            'lastname' : lastname,
            'email' : email,
            'address' :address,
            'age' : age,
            'gender' : gender,
            'contactnumber' : contactnumber,
            'emernumber' : emernumber, 
            'department' : department,
            'doctor' : doctor,
            'date' : date,
            'time' : time,
            'idz' : idz       
            }
        return render(request,'otp.html',context)
    return render(request,'newpatient.html')

def otp(request): 
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        contactnumber = request.POST.get('contactnumber')
        emernumber = request.POST.get('emernumber')
        department = request.POST.get('department')
        doctor = request.POST.get('doctor')
        date = request.POST.get('date')
        time = request.POST.get('time')
        idz = request.POST.get('idz')
        otp = request.POST.get('otp')
        try:
            onetime = Otp.objects.filter(patientid=idz).values()
        except:
            onetime = 0
        if onetime[0]['otp']==int(otp):
            patient = PatientDetails(patientid = idz,firstname = firstname,lastname=lastname,email=email,address=address,age=age,gender=gender,contact1=contactnumber,emgnumber=emernumber)
            patient.save()
            doc = Doctor.objects.filter(department=department,doctorname=doctor).values()
            doc_id = doc[0]['doctorid']
            print(doc_id)
            length = 0
            try:
                length = len(Booking.objects.filter(doctorid=doc_id,date=datetime.today()).values())
            except:
                pass
            book = Booking(patientid=idz,doctorid=doc_id,doctorname=doctor,department=department,date = date,time=time,token=length+1)
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
        else:
            return HttpResponse('<h1>invalid otp</h1>')    

def otpext(request):
     if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        contactnumber = request.POST.get('contactnumber')
        emernumber = request.POST.get('emernumber')
        idz = request.POST.get('idz')
        otp = request.POST.get('otp')
        try:
            onetime = Otp.objects.filter(patientid=idz).values()
        except:
            onetime = 0
        if onetime[0]['otp']==int(otp):
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




def extpatient(request):
    if request.method == "POST":
        patientid = request.POST.get('patientid')
        otp = random.randint(10000,1000000)
        
        patientdetails = PatientDetails.objects.filter(patientid = patientid).values()
        sms("+91"+str(patientdetails[0]['contact1']),'your otp is '+str(otp))
        onetime = Otp(patientid=patientid,otp=otp)
        onetime.save() 
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
        
        return render(request,'otpext.html',context)
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
    return render(request,'departments.html')

def contacts(request):
    return render(request,'contact.html')

def patientbooking(request):
    if request.method=="POST":
        patientid = request.POST.get('patientid')
        department = request.POST.get('department')
        doctor = request.POST.get('doctor')
        date = request.POST.get('date')
        time = request.POST.get('time')
        doc = Doctor.objects.filter(department=department,doctorname=doctor).values()
        doc_id = doc[0]['doctorid']
        length = 0
        try:
            length = len(Booking.objects.filter(doctorid=doc_id,date=datetime.today()).values())
        except:
            pass
        book = Booking(patientid=patientid,doctorid=doc_id,doctorname=doctor,department=department,date = date,time=time,token=length+1)
        book.save()
        bookingdetails = Booking.objects.filter(patientid=patientid).values()
        context = {
            'bookingdetails' : bookingdetails
        }
        return render(request,'bookings.html',context)