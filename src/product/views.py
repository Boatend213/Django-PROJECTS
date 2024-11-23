from django.shortcuts import render

from .models import product


# Create your views here.

def ShowHome(request):
    products = product.objects.all()
    return render(request,'product/index.html',{"football": products})


def Contact(request):
    return render(request,'product/Contact.html',{"key": "Date from datebase"})


def About(request):
    return render(request,'product/About.html',{"key": "Date from datebase"})

def create(request):
    return render(request,'product/create.html',{"key": "Date from datebase"})

def Events(request):
    return render(request,'product/Events.html',{"key": "Date from datebase"})


def Learn (request):
    return render(request,'product/Learn.html',{"key": "Date from datebase"})

def Register (request):
    return render(request,'product/Register.html',{"key": "Date from datebase"})

def Services (request):
    return render(request,'product/Services.html',{"key": "Date from datebase"})
def Highlight(request):
    return render(request,'product/Highlight Videos.html',{"key": "Date from datebase"})







