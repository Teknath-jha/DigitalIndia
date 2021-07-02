from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')




def feeDetails(request):
    return HttpResponse("we are at fee details")

def result(request):
    return HttpResponse("we are at result")



