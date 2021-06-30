from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def aboutDevelopers(request):
    return render(request,'aboutDevelopers.html')

def contactUs(request):
    return render(request,'contactUs.html')

def events(request):
    return HttpResponse(" we are at events  ")

def facilities(request):
    return HttpResponse(" we are at facilities  ")

def feeStructure(request):
    return HttpResponse(" we are at feeStructure")
