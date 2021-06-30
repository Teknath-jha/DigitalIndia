from django.db import models

# Create your models here.

class Student(models.Model):
    s_id         =  models.AutoField
    s_rollNo     = models.CharField(max_length=10)
    s_name       = models.CharField(max_length=50)
    s_father     = models.CharField(max_length=50)
    s_surname    = models.CharField(max_length=50)
    s_mother    = models.CharField(max_length=50)
    s_phone      = models.CharField( max_length=10)
    s_standard =models.CharField( max_length=20)
    s_age     = models.IntegerField()
    s_birth   = models.DateField()
    s_address = models.CharField(max_length=500)
    s_gender  = models.CharField( max_length=20)
    s_email   = models.EmailField(max_length=254,default="")
    s_password  = models.CharField( default="admin" , max_length=50)
 