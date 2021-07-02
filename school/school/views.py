from django.shortcuts import render
from django.http import HttpResponse
from student.models import Student
from teachingStaff.models import Teacher
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# from student.models import Post
# from user_profile.models import User


# Create your views here.

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def aboutDevelopers(request):
    return render(request, 'aboutDevelopers.html')


def contactUs(request):
    return render(request, 'contactUs.html')


def register(request):
    print("inside register ")
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        rollNo = request.POST['rollNo']
        username = request.POST['username']
        fatherName = request.POST['fatherName']
        surname = request.POST['surname']
        motherName = request.POST['motherName']
        phone = request.POST['phone']
        standard = request.POST['standard']
        age = request.POST['age']
        dob = request.POST['dob']
        gender = request.POST['gender']
        address = request.POST['address']
        email = request.POST['email']
        studentPassword = request.POST['studentPassword']
        Student(s_rollNo=rollNo,  username=username, s_father=fatherName, s_surname=surname, s_mother=motherName, s_phone=phone, s_standard=standard, s_age=age,
                s_birth=dob, s_gender=gender, s_address=address, s_email=email, password=studentPassword).save()
        print("student register hogay bhai ")
        return HttpResponse("Added ")

def registerTeacher(request):
    print("inside registerTeacher ")
    if request.method == 'GET':
        print("inside get ")
        return render(request, 'registerTeacher.html')
    if request.method == 'POST':
        print("inside post ")
        t_teacher=request.POST.get('t_teacher','False')
        username=request.POST['username']
        password=request.POST['teacherPassword']

        english=request.POST.get('english','False')
        maths=request.POST.get('maths','False')
        science=request.POST.get('science','False')
        socialScience=request.POST.get('socialScience','False')
        hindi=request.POST.get('hindi','False')
        marathi=request.POST.get('marathi','False')
        
        std1=request.POST.get('std1','False')
        std2=request.POST.get('std2','False')
        std3=request.POST.get('std3','False')
        std4=request.POST.get('std4','False')
        std5=request.POST.get('std5','False')
        std6=request.POST.get('std6','False')
        std7=request.POST.get('std7','False')
        std8=request.POST.get('std8','False')
        std9=request.POST.get('std9','False')
        std10=request.POST.get('std10','False')
        jrkg=request.POST.get('jrkg','False')
        srkg=request.POST.get('srkg','False')


        if t_teacher == 'on':
            t_teacher=True
        
        if english == 'on':
            english=True
        if maths == 'on':
            maths=True
        if  science== 'on':
            science=True
        if  socialScience == 'on':
            socialScience=True
        if  hindi== 'on':
            hindi=True
        if  marathi== 'on':
            marathi=True

        if std1 == 'on':
            std1=True
        if std2 == 'on':
            std2=True
        if std3 == 'on':
            std3=True
        if std4 == 'on':
            std4=True
        if std5 == 'on':
            std5=True
        if std6 == 'on':
            std6=True
        if std7 == 'on':
            std7=True
        if std8 == 'on':
            std8=True
        if std9 == 'on':
            std9=True
        if std10 == 'on':
            std10=True
        if srkg == 'on':
            srkg=True
        if jrkg == 'on':
            jrkg=True
        
        Teacher(t_teacher=t_teacher ,t_name=username , password=password , english=english , maths=maths , science=science , socialScience=socialScience , 
        hindi=hindi , marathi=marathi , std1=std1,std2=std2,std3=std3,std4=std4,std5=std5,std6=std6,std7=std7,std8=std8,std9=std9,std10=std10,
        stdJr=jrkg , stdSr=srkg).save()

        print("Teacher is added ")
        return HttpResponse("Teacher added <a href='/'>go to back</a> ")

# loggedinStudent=None
def handlelogin(request):
    if request.method == 'POST':
        # get post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        flagStudent = False
        # fetch all records from student table of Student schema model
        stu = Student.objects.all()
        stud=Student.objects.none()
        for x in stu:
            print(x.username + " " + x.password)
            if x.username == loginusername and x.password == loginpassword:
                print("match kargaya re ye to student hai  ")
                stud=x
                flagStudent = True
                break
        global loggedinStudent
        def loggedinStudent():
            return stud
        
        flagTeacher = False
        # fetch all records from student table of Student schema model
        tea = Teacher.objects.all()
        tead=Teacher.objects.none()
        for x in tea:
            print(x.t_name + " " + x.password)
            if x.t_name == loginusername and x.password == loginpassword:
                print("match kargaya re ye to sir hai  ")
                flagTeacher = True
                tead=x
                break
        global loggedinTeacher
        def loggedinTeacher():
            return tead
        
        
        # usrt={'username':loginusername}
        usrp={'username':"Principal"}
        # stud=Student.objects.filter(username=loginusername)
        print("stud here bro ")
        
        # Student loggin would be here
        if flagStudent == True:
            messages.success(request, "Logged In")
            print("student  logged in")
            usr={}
            usr['stud']=stud
            return render(request, 'assignments.html',usr)

        # Teacher loggin would be here
        elif flagTeacher == True:
            messages.success(request, "Logged In")
            print("Teacher  logged in")
            usrt={}
            usrt['tead']=tead
            return render(request, 'classes.html',usrt)

        # principal loggin
        elif user is not None:
            login(request, user)
            messages.success(request, "Logged In")
            return render(request, 'principalPage.html',usrp)

        else:
            print("not authorized by if block " + loginusername + "  ")
            messages.warning(request, "Invalid credentials ! ")
            return render(request, 'login.html')
    if request.method == 'GET':
        print("get at login")
        return render(request, 'login.html')
    return render(request, 'assignments.html')


def handlelogout(request):
    logout(request)
    messages.success(request, "Logged out ")
    return render(request, 'login.html')


def events(request):
    return HttpResponse(" we are at events  ")


def facilities(request):
    return HttpResponse(" we are at facilities  ")


def feeStructure(request):
    return HttpResponse(" we are at feeStructure")

def classesDetails(request):
    tead=loggedinTeacher()
    tead1={}
    tead1['tead']=tead
    return render(request,'classes-details.html',tead1)

def classes(request):
    return render(request,'classes.html')


def assignments(request):
    return render(request,'assignments.html')

def assignmentDetails(request):
    common={}
    try:
        stud=loggedinStudent()
        # common={}
        # common['tead']=tead
        common['stud']=stud
        return render(request,'assignmentDetails.html',common)
    except:
        tead=loggedinTeacher()
        # common={}
        common['tead']=tead
        # common['stud']=stud
        return render(request,'assignmentDetails.html',common)