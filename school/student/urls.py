from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path("",views.index,name='studentHome'),
    path("login/",views.login,name='login'),
    path("assignments/",views.assignments,name='assignments'),
    path("feeDetails/",views.feeDetails ,name='feeDetails'),
    path("results/",views.result ,name='result'),
]
