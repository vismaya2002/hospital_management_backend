from django.db import models
#from django.contrib.auth.models import User


class PatientDetails(models.Model):
    patientid = models.CharField(max_length=20)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=30)
    age = models.IntegerField()
    contact1 = models.IntegerField()
    emgnumber = models.IntegerField()





