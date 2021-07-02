from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path("",views.index,name='studentHome'),
    
    path("feeDetails/",views.feeDetails ,name='feeDetails'),
    path("results/",views.result ,name='result'),

]
