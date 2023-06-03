from django.db import models

# Create your models here.

class Doctor(models.Model):
    doctorid = models.CharField(max_length=30,primary_key=True)
    doctorname = models.CharField(max_length=30)
    department = models.CharField(max_length=30)



