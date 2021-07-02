"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index , name='index'),
    path('about/',views.about , name='about'),
    path('aboutDevelopers/',views.aboutDevelopers , name='aboutDevelopers'),
    path("assignments/",views.assignments,name='assignments'),
    path("assignmentDetails/",views.assignmentDetails,name='assignmentDetails'),
    path('login',views.handlelogin , name='handlelogin'),
    path('logout/',views.handlelogout , name='handlelogout'),
    path('register',views.register , name='register'),
    path('registerTeacher',views.registerTeacher , name='registerTeacher'),
    path('events/',views.events, name='events'),
    path('contactUs/',views.contactUs , name='contactUs'),
    path('facilities/',views.facilities, name='facilities'),
    path('feeStructure/',views.feeStructure, name='feeStructure'),
    path('classes/',views.classes, name='classes'),
    path('classesDetails/',views.classesDetails, name='classesDetails'),
    path("student/",include('student.urls')),                         #includeing entire app os student
    path("teachingStaff/",include('teachingStaff.urls'))
]
