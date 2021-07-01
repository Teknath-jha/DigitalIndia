from django.db import models

# Create your models here.

class Teacher(models.Model):
    t_id=models.AutoField
    t_name=models.CharField( max_length=100)
    password=models.CharField( max_length=50,default="teacher")

    english=models.BooleanField(default=False)
    maths=models.BooleanField(default=False)
    science=models.BooleanField(default=False)
    socialScience=models.BooleanField(default=False)
    hindi=models.BooleanField(default=False)
    marathi=models.BooleanField(default=False)

    std1=models.BooleanField(default=False)
    std2=models.BooleanField(default=False)
    std3=models.BooleanField(default=False)
    std4=models.BooleanField(default=False)
    std5=models.BooleanField(default=False)
    std6=models.BooleanField(default=False)
    std7=models.BooleanField(default=False)
    std8=models.BooleanField(default=False)
    std9=models.BooleanField(default=False)
    std10=models.BooleanField(default=False)
    stdJr=models.BooleanField(default=False)
    stdSr=models.BooleanField(default=False)
    # s_image = models.ImageField( upload_to="student/images",default="")
    
    def __str__(self): 
        return self.t_name 