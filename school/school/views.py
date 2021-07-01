from django.shortcuts import render
from django.http import HttpResponse
from student.models import Student
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
# from student.models import Post
# from user_profile.models import User


# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def aboutDevelopers(request):
    return render(request,'aboutDevelopers.html')

def contactUs(request):
    return render(request,'contactUs.html')

def register(request):
    print("inside register ")
    if request.method =='GET':
        return render(request,'register.html')
    if request.method == 'POST':
        rollNo = request.POST[ 'rollNo' ]
        username = request.POST[ 'username' ]
        fatherName = request.POST[ 'fatherName' ]
        surname= request.POST[ 'surname' ]
        motherName = request.POST[ 'motherName' ]
        phone = request.POST[ 'phone' ]
        standard = request.POST[ 'standard' ]
        age = request.POST[ 'age' ]
        dob = request.POST[ 'dob' ]
        gender = request.POST[ 'gender' ]
        address = request.POST[ 'address' ]
        email = request.POST[ 'email' ]
        studentPassword = request.POST[ 'studentPassword' ]
        Student(s_rollNo=rollNo ,  username = username ,s_father=fatherName,s_surname=surname,s_mother=motherName,s_phone=phone,s_standard=standard,s_age=age,
        s_birth=dob,s_gender=gender,s_address=address,s_email=email,password=studentPassword).save()
        print("student register hogay bhai ")
        return HttpResponse("Added ")
    



        


def handlelogin(request):
    if request.method=='POST':
        #get post parameters 
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user = authenticate(username=loginusername,password=loginpassword)
        flag=False
        # fetch all records from student table of Student schema model
        stu=Student.objects.all()
        for x in stu:
            print(x.username + " "  + x.password)
            if x.username==loginusername and x.password==loginpassword:
                print("match kargaya re ")
                flag=True
        
        #principal loggin
        if user is not None:
            login(request,user)
            messages.success(request,"Logged In")
            return render(request , 'register.html')
        #Student loggin would be here 
        elif flag==True:
            messages.success(request,"Logged In")
            return render(request , 'assignments.html')

        else:
            print("not authorized by if block " + loginusername + "  ")
            messages.warning(request,"Invalid credentials ! ")
            return render(request , 'login.html')
    if request.method == 'GET':
        print("get at login")
        return render(request,'login.html')
    return render(request,'assignments.html')

def handlelogout(request):
    logout(request)
    messages.success(request,"Logged out ")
    return render(request,'login.html')



def events(request):
    return HttpResponse(" we are at events  ")

def facilities(request):
    return HttpResponse(" we are at facilities  ")

def feeStructure(request):
    return HttpResponse(" we are at feeStructure")
