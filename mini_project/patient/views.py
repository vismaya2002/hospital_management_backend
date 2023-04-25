from django.shortcuts import render
from .models import PatientDetails,Booking
from doctor.models import Doctor
import random
'''from django.contrib.auth.models import User
from .models import addInfo
from django.contrib.auth import authenticate,login
from django.contrib.admin.forms import AuthenticationForm
# Create your views here.'''


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
    return render(request,'newpatient.html')

def extpatient(request):
    return render(request,'extpatient.html')





'''def signin(request):
    if request.user.is_authenticated:
        return render(request,'patientprofile.html')
    if request.method == 'POST':
        uzername = request.POST.get('username')
        pazzword = request.POST.get('password')
        print(uzername,pazzword)
        uzer = authenticate(request,username=uzername,password=pazzword)
        print(uzer)
        if uzer is not None:
            print("hai")
            login(request,uzer)
            return render(request,'patientprofile.html')
    return render(request,'Sign_In.html')
def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('profile')
    else:  
        form = AuthenticationForm()
    return render(request, 'Sign_In.html')

def register(request):
    if request.method=='POST':
        username= request.POST['username']
        password = request.POST['password']
        password2 = request.POST['confirmPassword']
        firstname = request.POST['firstName']
        lastname = request.POST['lastName']
        email = request.POST['email']
        address = request.POST['address']
        state = request.POST['state']
        city = request.POST['city']
        contact1 = request.POST['contact1']
        contact2 = request.POST['contact2']
        if password==password2:
            user= User.objects.create_user(username=username,password=password)
            user.save()
            info = addInfo.objects.create(user=user,email=email,first_name=firstname,last_name=lastname,address=address,city=city,state=state,contact1=contact1,contact2=contact2)
            info.save()
    return render(request,'Register.html')

def book(request):
    return render(request,'bookanappointment.html')

def profile(request):
    return render(request,'patientprofile.html')
'''

