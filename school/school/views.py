from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse(" we are at about  ")

def contact(request):
    return HttpResponse(" we are at contact us ")

def events(request):
    return HttpResponse(" we are at events  ")

def facilities(request):
    return HttpResponse(" we are at facilities  ")

def feeStructure(request):
    return HttpResponse(" we are at feeStructure")
