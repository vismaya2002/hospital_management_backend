from django.db import models
#from django.contrib.auth.models import User


class PatientDetails(models.Model):
    patientid = models.CharField(max_length=20,primary_key=True)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=30)
    age = models.IntegerField()
    contact1 = models.IntegerField()
    emgnumber = models.IntegerField()

 


class Booking(models.Model):
    patientid = models.CharField(max_length=20)
    doctorid = models.CharField(max_length=20)
    doctorname = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    date = models.DateField()
    time = models.TimeField()
    token = models.IntegerField()
    symptoms = models.TextField(default='')
    prescription = models.TextField(default='')
    remedies = models.TextField(default='')
