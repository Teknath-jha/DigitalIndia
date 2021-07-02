from django.db import models

# Create your models here.

class Student(models.Model):
    s_id         =  models.AutoField
    s_rollNo     = models.CharField(max_length=10)
    username       = models.CharField(max_length=50)
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
    password  = models.CharField( default="admin" , max_length=50)
    # s_image = models.ImageField( upload_to="student/images",default="")
    
    # def __str__(self):
    #     name=self.username + " r->" +self.s_rollNo + " std->"+ self.s_standard
    #     return name

class class10(models.Model):
    c_id=models.AutoField
    eng=models.CharField( max_length=254)
    mat=models.CharField( max_length=254)
    sci=models.CharField( max_length=254)
    sosci=models.CharField( max_length=254)
    hin=models.CharField( max_length=254)
    mar=models.CharField( max_length=254)

class class9(models.Model):
    c_id=models.AutoField
    eng=models.CharField( max_length=254)
    mat=models.CharField( max_length=254)
    sci=models.CharField( max_length=254)
    sosci=models.CharField( max_length=254)
    hin=models.CharField( max_length=254)
    mar=models.CharField( max_length=254)

class class8(models.Model):
    c_id=models.AutoField
    eng=models.CharField( max_length=254)
    mat=models.CharField( max_length=254)
    sci=models.CharField( max_length=254)
    sosci=models.CharField( max_length=254)
    hin=models.CharField( max_length=254)
    mar=models.CharField( max_length=254)

class class7(models.Model):
    c_id=models.AutoField
    eng=models.CharField( max_length=254)
    mat=models.CharField( max_length=254)
    sci=models.CharField( max_length=254)
    sosci=models.CharField( max_length=254)
    hin=models.CharField( max_length=254)
    mar=models.CharField( max_length=254)

class class6(models.Model):
    c_id=models.AutoField
    eng=models.CharField( max_length=254)
    mat=models.CharField( max_length=254)
    sci=models.CharField( max_length=254)
    sosci=models.CharField( max_length=254)
    hin=models.CharField( max_length=254)
    mar=models.CharField( max_length=254)